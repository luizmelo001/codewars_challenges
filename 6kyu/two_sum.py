"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, 
when added together, give the target value. 
The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).
For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Input: An array of numbers and a target number.
Output: The indexes of the two numbers that add up to the target number, returned as a

Algorithm:
    1. Create a dictionary to store the numbers and their corresponding indexes.
    2. Iterate through the array of numbers:
    a. For each number, calculate the complement by subtracting the current number from the target.
    b. Check if the complement exists in the dictionary:
        i. If it exists, return the current index and the index of the complement from the dictionary.
    c. If it does not exist, add the current number and its index to the dictionary.
    3. If no solution is found after iterating through the array, return None or an appropriate value indicating no solution exists.    

"""

def two_sums(numbers, target):
    num_dict = {}
    
    for index, num in enumerate(numbers):
        complement = target - num
        
        if complement in num_dict:
            return (num_dict[complement], index)
        
        num_dict[num] = index
    
    return None  # Return None if no solution is found  

print(two_sums([1, 2, 3], 4))
print(two_sums([1234, 5678, 9012], 14690))
print(two_sums([2, 2, 3], 4))