# 7. Deleting a File
# You can delete a file using the os.remove() function.

import os

if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("File deleted.")
else:
    print("File does not exist.")
    
# Remove the folder "myfolder":

import os
os.rmdir("myfolder")