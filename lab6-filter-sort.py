# Nik Myers
# IT-140 - Lab 6.13

# Get user input
init_input = input()

# Split initial input into a list of integers
ints = list(map(int, init_input.split()))

# Strip negative numbers from integer list
pos_ints = [i for i in ints if (i >= 0)]
# Sort new list in ascending order
pos_ints_sorted = sorted(pos_ints)

# Print each integer with trailing space and no newline
for integer in pos_ints_sorted:
    print(f'{integer} ', end='')
