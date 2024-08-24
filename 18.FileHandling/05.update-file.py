# 5. Updating Specific Lines in a File
# Updating a specific line in a file generally involves reading the entire file, modifying the content, and then writing it back.

# Reading the file into a list of lines
with open('example.txt', 'r') as file:
    lines = file.readlines()

# Updating a specific line (e.g., the second line)
lines[1] = "This is the updated second line.\n"

# Writing the updated lines back to the file
with open('example.txt', 'w') as file:
    file.writelines(lines)