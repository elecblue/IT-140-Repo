word = input()
password = ''

# Iterate over inputted word
for char in word:
   # Replace character and add to password variable
   if char == 'i':
      password += '!'
   elif char == 'a':
      password += '@'
   elif char == 'm':
      password += 'M'
   elif char == 'B':
      password += '8'
   elif char == 'o':
      password += '.'
   else:
      # Add original character if not in list
      password += char
else:
   # Add q*s to end of password and print
   password += 'q*s'
   print(password)
