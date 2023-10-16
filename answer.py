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
