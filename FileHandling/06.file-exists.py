# 6. Checking if a File Exists
# Before performing file operations, it's a good practice to check if the file exists.

import os

if os.path.exists('example.txt'):
    print("File exists.")
else:
    print("File does not exist.")