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