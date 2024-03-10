file_system = {"root": {"is_directory": True, "children": {}}}
current_directory = file_system["root"]

while True:
    command = input("Enter command (ls, mkdir, cd, touch, exit): ").split()

    if command[0] == "exit":
        break
    elif command[0] == "ls":
        for item in current_directory["children"]:
            print(item)
    elif command[0] == "mkdir" and len(command) > 1:
        new_directory = {"is_directory": True, "children": {}}
        current_directory["children"][command[1]] = new_directory
    elif command[0] == "cd" and len(command) > 1:
        if command[1] == "..":
            if current_directory != file_system["root"]:
                current_directory = file_system["root"]
        elif command[1] in current_directory["children"]:
            current_directory = current_directory["children"][command[1]]
    elif command[0] == "touch" and len(command) > 1:
        new_file = {"is_directory": False}
        current_directory["children"][command[1]] = new_file
    else:
        print("Invalid command. Try again.")

print("File system simulation ended.")
