from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
      ),
    },
  ),
)

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description="Gets text content of the specified file_path, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The file path to get file content from, relative to the working directory.",
      ),
    },
  ),
)

schema_run_python_file = types.FunctionDeclaration(
  name="run_python_file",
  description="Runs a Python file located at the specified file_path, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The file path of the Python file to run, relative to the working directory.",
      ),
    },
  ),
)

schema_write_file = types.FunctionDeclaration(
  name="write_file",
  description="Writes or overwrites the specified content to a file located at the specified file_path, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The file path of the file to write to, relative to the working directory.",
      ),
      "content": types.Schema(
        type=types.Type.STRING,
        description="The text content to write to the file at the specified file_path.",
      ),
    },
  ),
)