filename = "story.txt"

try:
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write to a new file
    with open("story_modified.txt", "w") as new_file:
        new_file.write(modified_content)

    print("File has been read and modified successfully!")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
