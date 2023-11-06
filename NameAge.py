# IT-140
# 2-3 Assignment: PyCharm Introduction
# Nik Myers

user_name = input('What is your name? ')
user_age = int(input('How old are you? '))
birth_year = 2023 - user_age  # Age isn't enough info to calculate birth year, but here's a guess.

print('\nHello {}! You were born in {}.'.format(user_name, birth_year))
