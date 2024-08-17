# 2. Writing to a File
# Writing to a file can be done using the write() method or the writelines() method for multiple lines.

# Writing a single line to the file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")

# Writing multiple lines to the file
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)