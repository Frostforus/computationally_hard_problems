import copy
import re

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
def print_all():
    print("k:", k)
    print("s String :", s)
    print("t_strings:", t_strings)
    print("R_subsets:", R_subsets)

print_all()



def alphabet_prune(k,s,t_strings,R_subsets):
    prunes = 0
    alphabet_s = set(s)

    new_R_subsets = dict()

    for R in R_subsets:
        new_R_subsets[R] = []
        for r in R_subsets[R]:
            prune = False
            for letter in r:
                if not prune and letter not in alphabet_s:
                    #print(f"r: {r}: letter {letter} not in alphabet {alphabet_s}")
                    prune = True
            if not prune:
                new_R_subsets[R].append(r)

    R_subsets =  copy.deepcopy(new_R_subsets)

    return k,s,t_strings,R_subsets

print(len(s))


k,s,t_strings,R_subsets = alphabet_prune(k,s,t_strings,R_subsets)
print_all()
print("Pruning done..")
