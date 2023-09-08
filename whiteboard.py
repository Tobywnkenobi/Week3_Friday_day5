"""
Fill the 5 lite jug to the top

Pour the 5 liter jug into the 3 liter jug, until full.  (2 liters in the 5 gallon jug)

empty the 3 liter jug into the garden

now we have and empty 3 liter jug, and a 5 liter jug with 2 liters left

Pour the 2 liters into the 3 liter jug.  (3 liter jug has 2 liters in it.  The 5 gallon is empty)

Fill the 5 liter jug to the top again

Pour the 5 liter jug into the 3 liter until full.  Pour out the 3 liter jug, and that leaves a 5 liters jug with 4 liters in it.


no 2

Problem Statement
You are given a list of coin denominations (e.g., `[1, 5, 10]` for pennies, nickels, and dimes) and a target amount of money (e.g., `18` cents). Write a Python function to find the minimum number of coins needed to make up the target amount. If it's not possible to make the exact amount, return `-1`.

min_coins([1, 2, 5], 11)  # Output: 3 (11 = 5 + 5 + 1)
min_coins([2], 3)  # Output: -1 (No combination can sum to 3)

coins : A list of integers where each integer represents the denomination of a coin. For example, [1, 5, 10] would mean you have coins of 1 cent (penny), 5 cents (nickel), and 10 cents (dime).

"""
def min_coins(coins, amount):
    
    coins.sort(reverse=True)
    
    total_coins = 0
    remaining_amount = amount

    for c in coins:
        n_coins = remaining_amount // c
        remaining_amount -= n_coins * c
        total_coins += n_coins
        
        if remaining_amount == 0:
            return total_coins

    return -1 if remaining_amount > 0 else total_coins

test1 = ([1, 2, 5], 11)  # Output: 3 (11 = 5 + 5 + 1)
test2 = ([2], 3)  # Output: -1 (No combination can sum to 3)

print(test1)
print(test2)