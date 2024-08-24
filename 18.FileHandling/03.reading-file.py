# 3. Reading from a File
# You can read from a file using the read(), readline(), or readlines() methods.

# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading the file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character
        
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()
  
# 
# 