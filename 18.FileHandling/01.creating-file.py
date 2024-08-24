# 1. Creating a File
# In Python, you can create a file using the open() function with the mode 'w' (write mode) or 'x' (exclusive creation).

# Creating a file using write mode
file = open('example.txt', 'w')
file.close()

# Creating a file using exclusive creation mode
try:
    file = open('example2.txt', 'x')
    file.close()
except FileExistsError:
    print("File already exists.")
