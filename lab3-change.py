#
# IT-140
# 3-2 Lab: Exact Change
# Nik Myers
#

# Get amount of change as input
amount = int(input())

# Coin definitions
coins = [(100, "Dollar"),
         (25, "Quarter"),
         (10, "Dime"),
         (5, "Nickel"),
         (1, "Penny")]

# Ignore inputs that can't be made into change
if amount <= 0:
   print('No change')
else:
   # Loop over coin definitions
   for coin in coins:
      value = coin[0]
      name = coin[1]

      # Divide amount of change by value of coin
      # and carry over remainder to next iteration
      if amount // value > 0:
         num_coins = amount // value
         amount %= value

         # Make coins plural if needed
         if num_coins > 1:
            if name.endswith('y'):
               name = name[:-1] + 'ies'
            else:
               name += 's'

         print(f'{num_coins} {name}')
