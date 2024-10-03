def write_to_file(filename, content):
  """
  Writes the provided content to the specified file.

  Args:
    filename: The name of the file to write to.
    content: The content to be written to the file.
  """
  try:
    with open(filename, "w") as file:
      file.write(content)
      print(f"Successfully wrote to {filename}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permission to write to '{filename}'.")
  finally:
    # This block will always execute, regardless of exceptions
    print("File writing operation completed.")

def read_from_file(filename):
  """
  Reads the contents of the specified file and displays them on the console.

  Args:
    filename: The name of the file to read from.
  """
  try:
    with open(filename, "r") as file:
      content = file.read()
      print(f"Contents of '{filename}':\n{content}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")   

  except PermissionError:
    print(f"Error: Insufficient permission to read from '{filename}'.")
  finally:
    print("File reading operation completed.")

def append_to_file(filename, content):
  """
  Appends the provided content to the specified file.

  Args:
    filename: The name of the file to append to.
    content: The content to be appended to the file.
  """
  try:
    with open(filename, "a") as file:
      file.write(content)
      print(f"Successfully appended to {filename}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permission to append to '{filename}'.")
  finally:
    print("File appending operation completed.")

# Create the file (if it doesn't exist) and write initial content
write_to_file("my_file.txt", "This is the first line.\n")
write_to_file("my_file.txt", "Here's some additional content with a number: 42\n")
write_to_file("my_file.txt", "The last line for initial creation.\n")

# Read the contents of the file
read_from_file("my_file.txt")

# Append additional content to the file
append_to_file("my_file.txt", "\nAppended line 1.\n")
append_to_file("my_file.txt", "Appended line 2 with another number: 100\n")
append_to_file("my_file.txt", "The final appended line.\n")

# Read the file again to see the appended content
read_from_file("my_file.txt")
