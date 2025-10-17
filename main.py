import os, sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.function_declarations import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from functions.get_files_info import get_files_info, get_file_content, run_python_file, write_file

WORKING_DIR = "./calculator"

def main():
  load_dotenv()
  
  verbose = "--verbose" in sys.argv
  args = []
  for arg in sys.argv[1:]:
    if not arg.startswith("--"):
      args.append(arg)
      
  if not args:
    print("AI Code Assistant")
    print('\nUsage: python main.py "your prompt here" [--verbose]')
    print('Example: python main.py "How do i build a calculator app?"')
    sys.exit(1)  
  
  api_key = os.environ.get("GEMINI_API_KEY")
  client = genai.Client(api_key=api_key)

  user_prompt = " ".join(args)
  
  if verbose:
    print(f'User prompt: {user_prompt}\n')

  messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
  ]
  
  for i in range(20):
    try:
      response = generate_content(client, messages, verbose)
      if response.text:
        print(response.text)
        break
    except Exception as e:
      print(f"Error generating content: {e}")
   

def generate_content(client, messages, verbose):
  
  system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
  """
  
  available_functions = types.Tool(
    function_declarations=[
      schema_get_files_info,
      schema_get_file_content,
      schema_run_python_file,
      schema_write_file,
    ]
  )
  
  response = client.models.generate_content(
    model="gemini-2.0-flash-001", 
    contents=messages,
    config=types.GenerateContentConfig(
      tools=[available_functions],
      system_instruction = system_prompt
    )
  )
  
  for candidate in response.candidates:
    messages.append(candidate.content)
  
  if verbose:
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
  
  if not response.function_calls:
    print(response.text)
  
  function_responses = []
  for function_call_part in response.function_calls:
      function_call_result = call_function(function_call_part, verbose)
      if (
          not function_call_result.parts
          or not function_call_result.parts[0].function_response
      ):
          raise Exception("empty function call result")
      if verbose:
          print(f"-> {function_call_result.parts[0].function_response.response}")
      function_responses.append(function_call_result.parts[0])
      messages.append(types.Content(role="user", parts=[types.Part(text=function_call_result.parts[0])]))

  if not function_responses:
      raise Exception("no function responses generated, exiting.")

def call_function(function_call_part, verbose=False):
    if verbose:
        print(
            f" - Calling function: {function_call_part.name}({function_call_part.args})"
        )
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    function_name = function_call_part.name
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR
    function_result = function_map[function_name](**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

if __name__ == "__main__":
    main()
