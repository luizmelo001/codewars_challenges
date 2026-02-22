"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

Input = "The narwhal bacons at midnight."
Output = "20 8 5 14 1 18 23 8
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz' 

def alphabet_position(text):
    return ' '.join(str(alphabet.index(c) + 1) for c in text.lower() if c in alphabet)


print(alphabet_position("The narwhal bacons at midnight."))