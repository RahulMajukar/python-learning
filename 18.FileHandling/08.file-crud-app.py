import os

def create_file():
    filename = input("Enter the filename to create: ")
    if os.path.exists(filename):
        print("File already exists.")
    else:
        with open(filename, 'w') as file:
            print(f"{filename} created successfully.")

def write_to_file():
    filename = input("Enter the filename to write to: ")
    if not os.path.exists(filename):
        print("File does not exist.")
    else:
        content = input("Enter the content to write to the file: ")
        with open(filename, 'w') as file:
            file.write(content)
        print("Content written to file successfully.")

def read_file():
    filename = input("Enter the filename to read: ")
    if not os.path.exists(filename):
        print("File does not exist.")
    else:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

def delete_file():
    filename = input("Enter the filename to delete: ")
    if not os.path.exists(filename):
        print("File does not exist.")
    else:
        os.remove(filename)
        print(f"{filename} deleted successfully.")

def crud_app():
    while True:
        print("\n--- CRUD Application ---")
        print("1. Create a new file")
        print("2. Write content to a file")
        print("3. Read from a file")
        print("4. Delete a file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_file()
        elif choice == '2':
            write_to_file()
        elif choice == '3':
            read_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    crud_app()
