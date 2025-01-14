with open('input.txt', 'r') as file: # put code on input.txt
    content = file.read()

# Count non-whitespace characters
non_whitespace_count = sum(1 for char in content if not char.isspace())

print(f"Number of non-whitespace characters: {non_whitespace_count}")