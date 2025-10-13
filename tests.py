from functions.get_files_info import get_files_info

def main():
  
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
  
  
  
if __name__ == "__main__":
    main()