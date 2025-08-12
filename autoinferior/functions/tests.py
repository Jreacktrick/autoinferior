import unittest
from get_files_info import get_files_info

class TestFileInfo(unittest.TestCase):
   
    def test_current_dir(self):
        current_dir_string = """Result for current directory:
         - main.py: file_size=576 bytes, is_dir=False
         - tests.py: file_size=1343 bytes, is_dir=False
         - pkg: file_size=92 bytes, is_dir=True"""
        
        result = get_files_info("calculator", ".")
        self.assertEqual(result, current_dir_string)

    def test_pkg_dir(self):
        current_dir_string = """Result for 'pkg' directory:
         - calculator.py: file_size=1739 bytes, is_dir=False
         - render.py: file_size=768 bytes, is_dir=False"""
        
        result = get_files_info("calculator", "pkg")
        self.assertEqual(result, current_dir_string)

    def test_bin_dir(self):
        current_dir_string = """Result for '/bin' directory:
        Error: Cannot list "/bin" as it is outside the permitted working directory"""
        
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, current_dir_string)

    def test_relative_dir(self):
        current_dir_string = """Result for '../' directory:
        Error: Cannot list "../" as it is outside the permitted working directory"""
        
        result = get_files_info("calculator", "../")
        self.assertEqual(result, current_dir_string)

if __name__ == "__main__":
    unittest.main()