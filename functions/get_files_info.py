import os, subprocess

def get_files_info(working_directory, directory = ""):
  
  try:
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not full_path.startswith(os.path.abspath(working_directory)):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    if not os.path.isdir(full_path):
      return f'Error: "{directory}" is not a directory\n'
    
    
    
    info = ""
    for file in os.listdir(full_path):
      filepath = os.path.join(full_path, file)
      info += f'- {file}: file_size={os.path.getsize(filepath)}, is_dir={os.path.isdir(filepath)}\n'
    
    return info
  
  except Exception as e:
    return f'Error: {e}'
    
def get_file_content(working_directory, file_path):
  try:
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'
    if not os.path.isfile(full_path):
      return f'Error: File not found or is not a regular file: "{file_path}"\n'
    
    MAX_CHARS = 10000
    
    with open(full_path, "r") as f:
      check_string = f.read()
      
    
    if len(check_string) > MAX_CHARS:
      with open(full_path, "r") as f:
        file_content_string = f'{f.read(MAX_CHARS)} [...File "{file_path}" truncated at 10000 characters]'
    else:
      file_content_string = check_string
    return file_content_string

  except Exception as e:
    return f'Error: {e}'

def write_file(working_directory, file_path, content):
  try:
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory\n'
    if not os.path.isfile(full_path):
      open(full_path, "w").close()
      
    with open(full_path, "w") as f:
      f.write(content)
      
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
      
  except Exception as e:
    return f'Error: {e}'
  
def run_python_file(working_directory, file_path, args=[]):
  try:
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory\n'
    if not os.path.isfile(full_path):
      return f'Error: File "{file_path}" not found.\n'
    if not file_path.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file.\n'
    
    
    commands = ["python", full_path]
    if args:
      commands.extend(args)

    response = ""
    completed_process = subprocess.run(commands, timeout=30, capture_output=True, text=True, cwd=abs_working_dir)
    if not completed_process:
      return "No output produced\n"
    response += f"STDOUT: {completed_process.stdout}\n"
    response += f"STDERR: {completed_process.stderr}\n"
    if completed_process.returncode:
      response += f"Process exited with code {completed_process.returncode}\n"
    return response
    
  except Exception as e:
    return f"Error: executing Python file: {e}\n"
    
