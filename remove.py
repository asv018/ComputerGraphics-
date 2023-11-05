import re

# Read the file contents
with open('Ludoboard.py', 'r') as f:
    contents = f.read()

# Remove comments using regex
contents = re.sub(r'^\s*#.*$', '', contents, flags=re.MULTILINE)

# Write the modified contents back to the file
with open('Ludoboard.py', 'w') as f:
    f.write(contents)
