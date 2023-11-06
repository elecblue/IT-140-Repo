# Nik Myers
# IT-140 - Lab 6.12

# Get user input
init_input = input()

# Split initial input into a list of integers
ints = list(map(int, init_input.split()))

# Calculate average of integers
average = int(sum(ints) / len(ints))
# Get max value from list of integers
max_int = max(ints)

# Print the average and max on one line separated by a space
print(f'{average} {max_int}')
