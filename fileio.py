import unittest
import os


# Problem 1: Write a function to write a string to a file.
def write_string_to_file(s, filename):
    with open(filename, 'w') as f:
        f.write(s)
        
# Problem 2: Write a function to read a string from a file.
def read_string_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# Problem 3: Write a function to append a string to a file.
def append_string_to_file(s, filename):
    with open(filename, 'a') as f:
        f.write(s)

# Problem 4: Write a function to copy contents from one file to another.
def copy_file_content(src, dest):
    with open(src, 'r') as fsrc, open(dest, 'w') as fdest:
        fdest.write(fsrc.read())
        
# Problem 5: Write a function to count the number of lines in a file.
def count_lines(filename):
    print(filename)
    with open(filename, 'r') as f:
        return len(f.readlines())

# Problem 6: Write a function to find a string in a file and return the line number.
def find_string_in_file(s, filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            if s in line:
                return i
    return None

# Problem 7: Write a function to delete a specific line from a file.
def delete_line(filename, line_number):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for i, line in enumerate(lines):
            if i != line_number - 1:
                f.write(line)

# Problem 8: Write a function to replace a specific line in a file.
def replace_line(filename, line_number, new_line):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for i, line in enumerate(lines):
            if i == line_number - 1:
                f.write(new_line + '\n')
            else:
                f.write(line)

# Problem 9: Write a function to get the size of a file.
def get_file_size(filename):
    return os.path.getsize(filename)

# Problem 10: Write a function to create a file with N lines of numbers from 1 to N.
def create_file_with_numbers(filename, N):
    with open(filename, 'w') as f:
        for i in range(1, N+1):
            f.write(str(i) + '\n')





def run_example_operations():
    print("Running example operations...\n")
    
    filename = "example.txt"
    filename_copy = "example_copy.txt"
    append_text = " Appended Text!"
    line_number = 3
    replacement_text = "This line has been replaced."
    
    # Example 1: write_string_to_file
    write_string_to_file("Hello, World!", filename)
    print(f"1. Written to {filename}: Hello, World!")
    
    # Example 2: read_string_from_file
    # read_content = read_string_from_file(filename)
    # print(f"2. Read from {filename}: {read_content}")
    
    # # Example 3: append_string_to_file
    # append_string_to_file(append_text, filename)
    # print(f"3. Appended to {filename}: {append_text}")
    # print(f"   New content: {read_string_from_file(filename)}")
    
    # # Example 4: copy_file_content
    # copy_file_content(filename, filename_copy)
    # print(f"4. Copied content from {filename} to {filename_copy}.")
    # print(f"   Content in {filename_copy}: {read_string_from_file(filename_copy)}")
    
    # # Example 5: count_lines
    # num_lines = count_lines(filename)
    # print(f"5. Number of lines in {filename}: {num_lines}")
    
    # # Example 6: find_string_in_file
    # string_to_find = "World"
    # line_found = find_string_in_file(string_to_find, filename)
    # print(f"6. String '{string_to_find}' found in {filename} at line: {line_found}")
    
    # # Example 7: delete_line
    # delete_line(filename, line_number)
    # print(f"7. Deleted line {line_number} from {filename}.")
    # print(f"   New content: {read_string_from_file(filename)}")
    
    # # Example 8: replace_line
    # replace_line(filename, line_number, replacement_text)
    # print(f"8. Replaced line {line_number} in {filename} with: {replacement_text}")
    # print(f"   New content: {read_string_from_file(filename)}")
    
    # # Example 9: get_file_size
    # file_size = get_file_size(filename)
    # print(f"9. Size of {filename}: {file_size} bytes")
    
    # Example 10: create_file_with_numbers
    create_file_with_numbers("numbers.txt", 5)
    print(f"10. Created a new file with numbers from 1 to 5.")
    print(f"    Content: {read_string_from_file('numbers.txt')}")

    
if __name__ == "__main__":
    run_example_operations()