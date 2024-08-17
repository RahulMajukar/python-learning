# 4. Appending to a File
# To add content to an existing file without overwriting it, use the 'a' (append) mode.

# Appending a line to the file
with open('example.txt', 'a') as file:
    file.write("Appended line.\n")

# Appending multiple lines to the file
more_lines = ["Another line\n", "Yet another line\n"]
with open('example.txt', 'a') as file:
    file.writelines(more_lines)