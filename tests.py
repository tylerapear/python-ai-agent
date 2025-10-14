from functions.get_files_info import get_files_info, get_file_content, write_file, run_python_file

def test_dirs():
  test1_results = get_files_info("calculator", ".")
  print(f'Results from current directory:')
  print(test1_results)
  
  test2_results = get_files_info("calculator", "pkg")
  print(f"Results from 'pkg' directory:")
  print(test2_results)
  
  test3_results = get_files_info("calculator", "/bin")
  print(f"Results from '/bin' directory:")
  print(test3_results)
  
  test4_results = get_files_info("calculator", "../")
  print(f"Results from '../' directory:")
  print(test4_results)
  
def test_files():
  test1_results = get_file_content("calculator", "main.py")
  print(f'Results from main.py:')
  print(test1_results)
  
  test2_results = get_file_content("calculator", "pkg/calculator.py")
  print(f"Results from 'pkg/calculator':")
  print(test2_results)
  
  test3_results = get_file_content("calculator", "/bin/cat")
  print(f"Results from '/bin/cat':")
  print(test3_results)
  
  test4_results = get_file_content("calculator", "pkg/does_not_exist.py")
  print(f"Results from 'pkg/does_not_exist.py':")
  print(test4_results)

def test_write():
  test1_results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
  print(f'Results from test1:')
  print(test1_results)
  
  test2_results = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
  print(f"Results from test2:")
  print(test2_results)
  
  test3_results = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
  print(f"Results from test3:")
  print(test3_results)
  
def test_run():
  test1_results = run_python_file("calculator", "main.py")
  print(f'Results from test1:')
  print(test1_results)
  
  test2_results = run_python_file("calculator", "main.py", ["3 + 5"])
  print(f"Results from test2:")
  print(test2_results)
  
  test3_results = run_python_file("calculator", "tests.py")
  print(f"Results from test3:")
  print(test3_results)
  
  test4_results = run_python_file("calculator", "../main.py")
  print(f"Results from test4:")
  print(test4_results)
  
  test5_results = run_python_file("calculator", "nonexistent.py")
  print(f"Results from test5:")
  print(test5_results)
  
  test6_results = run_python_file("calculator", "lorem.txt")
  print(f"Results from test6:")
  print(test6_results)

def main():
  test_run()
  
  
  
  
if __name__ == "__main__":
    main()