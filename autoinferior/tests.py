from functions.run_python_file import run_python_file
from functions.write_file import write_file
def test():
    result = run_python_file("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for current directory:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for current directory:")
    print(result)
    print("")

if __name__ == "__main__":
    test()



#import unittest
#from functions.get_files_info import get_files_info
#
#class TestFileInfo(unittest.TestCase):
#   
#    def test_current_dir(self):
#        expected = """- main.py: file_size=576 bytes, is_dir=False\n- tests.py: file_size=1343 bytes, is_dir=False\n- pkg: file_size=92 bytes, is_dir=True"""
#        
#        result = get_files_info("calculator", ".")
#        self.assertEqual(result, expected)
#
#    def test_pkg_dir(self):
#        expected = """- calculator.py: file_size=1739 bytes, is_dir=False\n- render.py: file_size=768 bytes, is_dir=False"""
#        
#        result = get_files_info("calculator", "pkg")
#        self.assertEqual(result, expected)
#
#    def test_bin_dir(self):
#        expected = """Error: Cannot list "/bin" as it is outside the permitted working directory"""
#        
#        result = get_files_info("calculator", "/bin")
#        self.assertEqual(result, expected)
#
#    def test_relative_dir(self):
#        expected = """Error: Cannot list "../" as it is outside the permitted working directory"""
#        
#        result = get_files_info("calculator", "../")
#        self.assertEqual(result, expected)
#
#if __name__ == "__main__":
#    unittest.main()