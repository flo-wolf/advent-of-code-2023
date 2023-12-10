import re

class Card:
    def __init__(self, winning_numbers: list[int], guesses: list[int]):
        self.winning_numbers = winning_numbers
        self.guesses = guesses

    def get_points() -> int:
        return 0

file = open('4_input.txt', 'r')
lines = file.readlines()

for line in lines:
    for match in re.finditer(r'(?:^|\|)\s*([0-9\s]+)\s*\|\s*([0-9\s]+)\s*(?:$|\|)', line, re.IGNORECASE):
        matched_winning_numbers, matched_guesses = match.groups()