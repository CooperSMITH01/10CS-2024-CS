import os

file_path = 'sports01.txt'

sports = []

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        sports = [line.strip() for line in file.readlines()]

new_sport = input('Enter your favourite sport: ')

if new_sport:
    sports.append(new_sport)

