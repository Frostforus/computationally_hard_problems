import re

text = "Hello, my email is example@email.com and my phone number is 123-456-7890."

email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phone_numbers = re.findall(phone_pattern, text)

print("Emails:", emails)
print("Phone Numbers:", phone_numbers)

# Array of strings to check
substring_array = ["apple", "banana", "cherry"]

# Target string to search within
target_string = "I like apples and cherries."

# Construct a regex pattern to match any of the substrings
pattern = "|".join(re.escape(substring) for substring in substring_array)

# Use re.search() to check for matches
match = re.search(pattern, target_string)

if match:
    print("Found a match:", match.group())
else:
    print("No match found.")

# Initialize variables
k = 0
s = ""
t_strings = []
R_subsets = {}

file_path = "../"
file_name = "test02.swe"

#TODO:

# Read the input file
with open(file_path+file_name, "r") as file:
    # Read the number k
    k = int(file.readline().strip())

    # Read the string s
    s = file.readline().strip()

    # Read the k strings t1, t2, ..., tk
    for _ in range(k):
        t = file.readline().strip()
        t_strings.append(t)

    # Read the sets of letters and their corresponding contents
    for line in file:
        if line.strip():  # Skip empty lines
            letter, content = line.split(":", 1)
            R_subsets[letter] = content.strip().split(",")

# Print the variables
print("k:", k)
print("s String :", s)
print("t_strings:", t_strings)
print("R_subsets:", R_subsets)


