import re

class Card:
    def __init__(self, winning_numbers: list[int], guesses: list[int]):
        self.winning_numbers = winning_numbers
        self.guesses = guesses

    def get_points(self) -> int:
        points = 0
        for guess in self.guesses:
            for winning_number in self.winning_numbers:
                if guess == winning_number:
                    if points == 0:
                        points = 1
                    else:
                        points = points * 2
        return points

file = open('4_input.txt', 'r')
lines = file.readlines()

total_points = 0
for line in lines:
    for match in re.findall(r': *(\d+(?:  ?\d+)*) \| *(\d+(?:  ?\d+)*)', line):
        winning_numbers = list(map(int, match[0].split()))
        guesses = list(map(int, match[1].split()))
        card = Card(winning_numbers, guesses)
        total_points += card.get_points()

print(total_points)