# Nik Myers
# IT-140 - Lab 6.18

# Get list of words from input
words_input = input()

# Split words into List
words = words_input.split()

# Initialize dict to hold words and frequency
words_tracker = {}

# Loop over words in list to count
for word in words:
    # Increment frequency if word exists in dict
    if word in words_tracker:
        words_tracker[word] += 1
    # Add word to dict with single freq if absent
    else:
        words_tracker[word] = 1

# Print each word and its frequency
# This iterates over the list in order to print repeated words
for word in words:
    print(f'{word} {words_tracker[word]}')
