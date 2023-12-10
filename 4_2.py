import re

class Card:
    def __init__(self, index: int, winning_numbers: list[int], guesses: list[int]):
        self.index = index
        self.winning_numbers = winning_numbers
        self.guesses = guesses
        self.copies = 1 # start with a single copy, i.e. just itself

    def get_win_count(self) -> int:
        win_count = 0
        for guess in self.guesses:
            for winning_number in self.winning_numbers:
                if guess == winning_number:
                    win_count += 1
        return win_count


def create_cards() -> list[Card]:
    cards: list[Card] = []
    file = open('4_input.txt', 'r')
    lines = file.readlines()
    card_index = 0
    for line in lines:
        for match in re.findall(r': *(\d+(?:  ?\d+)*) \| *(\d+(?:  ?\d+)*)', line):
            winning_numbers = list(map(int, match[0].split()))
            guesses = list(map(int, match[1].split()))
            cards.append(Card(card_index, winning_numbers, guesses))
        card_index += 1
    return cards

cards = create_cards()
total_card_count = len(cards)

for index, card in enumerate(cards):
    win_count = card.get_win_count()
    for copy in range(card.copies):
        for win in range(win_count):
            card_to_copy_index = index + win + 1
            if card_to_copy_index < len(cards):
                cards[card_to_copy_index].copies += 1
                total_card_count += 1

print(total_card_count)