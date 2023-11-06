import csv
from collections import defaultdict

# Get the CSV file from user input
filename = input()

# Using defaultdict(int) sets each key to zero by default
freqs = defaultdict(int)

# Open the file for reading using csv.reader()
# With closes the stream after reading is complete
with open(filename, 'r') as file:
    # Create CSV reader object with inputted file
    reader = csv.reader(file)

    # Parse through each row in CSV
    for row in reader:
        # Parse through each 'cell' in row
        for word in row:
            # Add/lookup key and add one to value
            freqs[word.strip()] += 1

# Loop through freqs dictionary and print each key and frequency
for word, freq in freqs.items():
    print(f"{word} {freq}")
