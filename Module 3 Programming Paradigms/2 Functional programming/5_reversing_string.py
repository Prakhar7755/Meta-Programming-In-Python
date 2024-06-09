#  str[start:stop:step]

""" USING SLICING """
trial = "reversal"

new_trial = trial[::-1]

print(new_trial)


""" RECURSION """

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

my_string = "Gamushara"
reversed_string = reverse_string(my_string)
print(reversed_string)  # Output: "olleh"


