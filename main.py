import copy
import re


# Initialize variables
class Variables:
    __slots__ = ("k", "s", "t_strings", "R_subsets")

    def __init__(self):
        self.t_strings = []
        self.R_subsets = {}

    def __str__(self):
        return f"Variables(k={self.k}, s={self.s}, t_strings={self.t_strings}, R_subsets = {self.R_subsets})"

    def check_lowercase(self):
        if not re.findall("^[a-z]*$", self.s):
            return False

        for R in self.R_subsets:
            for substring in self.R_subsets[R]:
                if not re.findall("^[a-z]*$", substring):
                    return False

        return True

    def get_variables_from_file(self, filename, filepath="./"):
        # Read the input file
        with open(filepath + filename, "r") as file:
            # Read the number k
            self.k = int(file.readline().strip())

            # Read the string s
            self.s = file.readline().strip()

            # Read the k strings t1, t2, ..., tk
            for _ in range(self.k):
                t = file.readline().strip()
                self.t_strings.append(t)

            # Read the sets of letters and their corresponding contents
            for line in file:
                if line.strip():  # Skip empty lines
                    letter, content = line.split(":", 1)
                    self.R_subsets[letter] = content.strip().split(",")

    def get_variables_from_input(self):
        try:
            self.k = int(input())
            if self.k < 0:
                return "NO"

            self.s = input()

            # t_strings
            for i in range(self.k):
                self.t_strings.append(input())

            # R_subsets
            while True:
                line = input()

                if not line.strip():
                    break

                if ":" in line:
                    letter, content = line.split(":", 1)
                    if letter in self.R_subsets.keys():
                        return "NO"
                    self.R_subsets[letter] = content.strip().split(",")
                else:
                    return "NO"
        except:
            # only used to catch fails
            pass

    def check_multiset(self):
        for R in self.R_subsets:
            if len(self.R_subsets[R]) != len(set(self.R_subsets[R])):
                return False

        return True

    def alphabet_prune(self, ):
        # TODO: count prunes if we want to
        # prunes = 0
        alphabet_s = set(self.s)
        alphabet_s.add("")
        new_R_subsets = dict()

        for R in self.R_subsets:
            new_R_subsets[R] = []
            for r in self.R_subsets[R]:
                prune = False
                for letter in r:
                    if not prune and letter not in alphabet_s:
                        # print(f"r: {r}: letter {letter} not in alphabet {alphabet_s}")
                        prune = True
                if not prune:
                    new_R_subsets[R].append(r)

        self.R_subsets = copy.deepcopy(new_R_subsets)
        # print("Pruning done.")


def is_substring(s, new_t_i):
    if s == "" and new_t_i == "":
        return True

    compiled_regex = re.compile(new_t_i)
    return compiled_regex.search(s) is not None


def find_solutions(s, t_strings, i, R_subsets, Gamma, substitutions):
    # if no gammas are left a solution has been found
    if i >= len(R_subsets.keys()):
        return substitutions

    gam = Gamma[i]

    # try all r
    for j in range(len(R_subsets[gam])):
        success = True
        new_t = []
        # apply substitution for each t
        for t_i in t_strings:
            new_t_i = ""
            test_t_i = r""
            for c in t_i:
                if c == gam:
                    new_t_i += R_subsets[gam][j]
                    test_t_i += R_subsets[gam][j]
                elif c in Gamma:
                    test_t_i += ".?"
                    new_t_i += c
                else:
                    new_t_i += c
                    test_t_i += c

            # test new_t_i
            isSubstring = is_substring(s, test_t_i)
            if not isSubstring:
                success = False
                break

            new_t.append(new_t_i)

        if success:
            substitutions[gam] = R_subsets[gam][j]
            result = find_solutions(s, new_t, i + 1, R_subsets, Gamma, substitutions)
            if result:
                return result
    return False


if __name__ == "__main__":
    try:

        variables = Variables()
        # variables.get_variables_from_file("test02.swe")
        correct_extraction = variables.get_variables_from_input()
        # test if non conforming input
        if correct_extraction == "NO" or not variables.check_lowercase() or not variables.check_multiset():
            print("NO")
        # solve the problem
        else:
            # print(variables)
            variables.alphabet_prune()
            # print(variables)

            result = find_solutions(variables.s, variables.t_strings, 0, variables.R_subsets,
                                    list(variables.R_subsets.keys()),
                                    {})
            if result:
                for k in result.keys():
                    print(k + ':' + result[k])
            else:
                if variables.s == "":
                    for k in variables.R_subsets.keys():
                        print(k + ':' )
                else:
                    print("NO")

    except Exception as e:
        print(f"NO")
