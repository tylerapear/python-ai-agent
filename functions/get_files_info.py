import os

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
    