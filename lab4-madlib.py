# Get prompt from input of noun and number then split into an array
prompt = input().split(' ')
# Assign noun and number into their own variables
noun = prompt[0]
num = int(prompt[1])

# Loop until the noun inputted is "quit"
while noun != 'quit':
   # Print funny mad lib with prompt inserted
   print('Eating {} {} a day keeps the doctor away.'.format(num, noun))
   # Get and assign prompt again to continue or quit loop
   prompt = input().split(' ')
   noun = prompt[0]
   num = int(prompt[1])