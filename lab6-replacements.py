# Nik Myers
# IT-140 - Lab 6.19

# Get words/replacements from input
words_input = input()
# Get sentence from input
sentence = input()

# Create list of word pairs split by double spaces
words_list = words_input.split('  ')
# Create an empty dictionary for word pairs
replacements = {}

# Iterate through word pairs and add them to the dictionary
for word in words_list:
    words = word.split()
    replacements[words[0]] = words[1]

# Iterate through the dictionary of word pairs and replace the words
for word, replacement in replacements.items():
    sentence = sentence.replace(word, replacement)

# Print out the updated sentence
print(f'{sentence}')
