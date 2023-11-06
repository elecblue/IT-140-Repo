# Coin definitions
coins = [(100, "dollar"),
         (25, "quarter"),
         (10, "dime"),
         (5, "nickel"),
         (1, "penny")]


# Get amount of change as input
def exact_change(user_total):
    output = []

    # Ignore inputs that can't be made into change
    if user_total <= 0:
        output = [0, 0, 0, 0, 0]
    else:
        # Loop over coin definitions
        for coin in coins:
            value = coin[0]

            # Divide amount of change by value of coin
            # and carry over remainder to next iteration
            if user_total // value >= 0:
                num_coins = user_total // value
                user_total %= value

                output.append(num_coins)

    return tuple(output)


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Print out the right denominations
    if input_val > 0:
        if num_dollars > 1:
            print(f'{num_dollars} dollars')
        elif num_dollars == 1:
            print(f'{num_dollars} dollar')

        if num_quarters > 1:
            print(f'{num_quarters} quarters')
        elif num_quarters == 1:
            print(f'{num_quarters} quarter')

        if num_dimes > 1:
            print(f'{num_dimes} dimes')
        elif num_dimes == 1:
            print(f'{num_dimes} dime')

        if num_nickels > 1:
            print(f'{num_nickels} nickels')
        elif num_nickels == 1:
            print(f'{num_nickels} nickel')

        if num_pennies > 1:
            print(f'{num_pennies} pennies')
        elif num_pennies == 1:
            print(f'{num_pennies} penny')
    else:
        print('no change')
