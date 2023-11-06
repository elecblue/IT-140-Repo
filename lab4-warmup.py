# Get character and height from input
triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

# Keep tally of lines printed
line = 1

# Add a line of padding before triangle
print('')

# Iterate until the number of lines matches the inputted height
while line <= triangle_height:
   # This is a right triangle, so each line needs that number of characters
   # For example: Line 2 has 2, line 3 has 3, etc.
   for i in range(line):
      print('{}'.format(triangle_char), end=' ')
   # Insert newline
   print('')
   # Add to line tally
   line += 1