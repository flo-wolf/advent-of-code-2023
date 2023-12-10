import re

class Set:
    def __init__(self, set_string: str):
        self.red = self._get_color_amount(set_string, "red")
        self.green = self._get_color_amount(set_string, "green")
        self.blue = self._get_color_amount(set_string, "blue")

    def _get_color_amount(self, set_string: str, color_name: str) -> int:
        color_match = re.findall(rf'(\d+) {color_name}', set_string)
        if len(color_match) > 0:
            return int(color_match[0])
        else:
            return 0

class Game:
    def __init__(self, line: str):
        self.id = self._parse_id(line)
        self.sets = self._parse_line_sets(line)

    def _parse_id(self, line: str) -> int:
        id_matches = re.findall(r'Game (\d+)\:', line)
        return int(id_matches[0])

    def _parse_line_sets(self, line: str) -> list[Set]:
        sets: list[Set] = []
        set_strings = re.findall(r'(?::|;)\s*(.*?)(?:(?=(?:;)|$))', line)
        for set_string in set_strings:
            sets.append(Set(set_string))
        return sets

    def is_possible(self, total_red: int, total_green: int, total_blue: int) -> bool:
        for set in self.sets:
            if set.red > total_red:
                return False
            if set.green > total_green:
                return False
            if set.blue > total_blue:
                return False
        return True


file1 = open('2_input.txt', 'r')
lines = file1.readlines()

game_id_sum = 0
for line in lines:
    game = Game(line)
    if game.is_possible(12, 13, 14):
        game_id_sum += game.id

print(game_id_sum)