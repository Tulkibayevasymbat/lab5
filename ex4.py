#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

def f(s):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, s)
    return sequences

s = input()
result = f(s)
print(result)