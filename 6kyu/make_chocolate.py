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
    # Step 1: Try to use as many big bars (5kg) as possible
    max_big_we_can_use = min(big, goal // 5)
    
    # Step 2: Try from the maximum number of big bars downwards
    for num_big in range(max_big_we_can_use, -1, -1):
        remaining_kg = goal - (num_big * 5)
        
        # If remaining can be exactly covered by small chocolates
        if remaining_kg <= small:
            return remaining_kg   # number of 1kg chocolates needed
    
    # If no combination worked
    return -1
    
print(make_chocolates(4, 1, 13))
print(make_chocolates(2, 1, 7))
print(make_chocolates(3, 1, 6))
