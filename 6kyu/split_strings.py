"""
Complete the solution so that it splits the string into strings of two characters in a list/array (depending on the language you use). If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

Input/Output
    Input: A string.
    Output: An array of strings.

Algorithm
    1. Initialize an empty list to hold the pairs.
    2. Iterate through the input string in steps of 2 characters.
    3. For each pair of characters, check if the second character exists.
    4. If it does, add the pair to the list.
    5. If it doesn't, add the first character followed by an underscore to the list.
"""

def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            pairs.append(s[i:i+2])
        else:
            pairs.append(s[i] + '_')
    return pairs

#one liner
#def solution(s):
#   return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

