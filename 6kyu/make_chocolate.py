"""
Write a function make_chocolates that will accept three integer values as arguments, in the following order:
small -> number of small chocolates available
big -> number of big chocolates available
goal -> the desired weight of the final parcel
The function should return the number of small chocolates required to achieve the goal. The function should return -1 only if the goal cannot be achieved by any possible combination of big chocolates and small chocolates.

Input:
      - three integers: small, big, goal
Output:
      - an integer representing the number of small chocolates required to achieve the goal, or -1 if the goal cannot be achieved
Example:        
        -make_chocolates(4, 1, 9) -> 4
        -make_chocolates(4, 1, 10) -> -1

"""

def make_chocolates(small, big, goal):

    remaining = goal % small
    counter = 0

    while goal > 0:
        goal -= small
        counter += 1
        print(f"goal: {goal}, remaining: {remaining}, counter: {counter}")

    if big > remaining:
        return -1
 
    return counter
    
print(make_chocolates(4, 1, 13))
print(make_chocolates(2, 1, 7))
print(make_chocolates(3, 1, 6))
