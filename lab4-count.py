user_text = input()
count = 0

# Iterate over each character in inputted string
for char in user_text:
   # Ignore if the character is a space, period, or comma
   if char.isspace() or (char == '.') or (char == ','):
      continue
   else:
      # Keep running tally of characters
      count += 1
else:
   # Print the resulting character count
   print(count)
