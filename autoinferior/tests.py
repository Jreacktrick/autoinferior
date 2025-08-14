
from functions.write_file import write_file
def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for current directory:")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for current directory:")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
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