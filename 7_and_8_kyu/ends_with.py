"""
Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false
"""

def ends_with(str, arg):
    return str.endswith(arg)

print(ends_with("abc", "bc"))
