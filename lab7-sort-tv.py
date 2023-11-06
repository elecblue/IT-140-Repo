# Nik Myers
# IT-140 - Lab 7.9

# Define function that reads inputted text file to dictionary
def read_to_dict(filename):
    # Open file at filename and close when finished reading
    with open(filename, 'r') as f:
        lines = f.readlines()
    # Create an empty dictionary
    tv_shows = {}
    # Read every other line as a key
    for i in range(0, len(lines), 2):
        num_seasons = int(lines[i].strip())
        show_name = lines[i + 1].strip()
        # If the key exists already, append that show title to the value
        if num_seasons in tv_shows:
            tv_shows[num_seasons].append(show_name)
        # If it doesn't, it's a key with that value
        else:
            tv_shows[num_seasons] = [show_name]
    # Return the tv_shows dictionary
    return tv_shows


# Define function that writes to a file sorted numerically by key
def write_by_keys(tv_shows, filename):
    # Open file or create new one with write permissions
    with open(filename, 'w') as f:
        # Loop through keys in ascending order
        for key in sorted(tv_shows.keys()):
            # Write key and value(s) separated by a colon, multiple vals joined by semicolon
            f.write(str(key) + ": " + "; ".join(tv_shows[key]) + "\n")


# Define function that writes to a file with only values sorted alphabetically
def write_by_titles(tv_shows, filename):
    # Created a dictionary sorted by each value alphabetically using Python's version
    # of an arrow function.
    sorted_dict = dict(sorted(tv_shows.items(), key=lambda item: item[1][0]))
    # Write values (joined by newline if multiple) to file or overwrite existing file
    with open(filename, 'w') as f:
        for key, value in sorted_dict.items():
            f.write("\n".join(value) + "\n")


# Define function that writes to a file with only values sorted alphabetically
def by_titles(tv_shows, filename):
    # Create empty list for show titles
    show_titles = []

    # Iterate through shows and extend to list
    for show in tv_shows.values():
        show_titles.extend(show)

    # Open file with write access or create new file
    with open(filename, 'w') as f:
        # Iterate through titles and write to file
        for title in sorted(show_titles):
            f.write(f'{title}\n')


# Get source filename as input from user
input_file = input()
# Read source file into a dictionary using defined function
shows = read_to_dict(input_file)

# Write output file sorted by keys
write_by_keys(shows, 'output_keys.txt')
# Write output file sorted by values alphabetically
by_titles(shows, 'output_titles.txt')
