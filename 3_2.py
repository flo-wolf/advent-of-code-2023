import re

LAST_LINE_CHARACTER_INDEX = 139

class Gear:
    def __init__(self, index: int, line_index: int):
        self.line_index: int = line_index
        self.index: int = index
        self.adjacent_numbers: set[Number] = set()

class Number:
    def __init__(self, value: int, line_index: int, start_index: int, end_index: int):
        self.value: int = value
        self.line_index: int = line_index
        self.start_index: int = start_index
        self.end_index: int = end_index

    def mark_adjacent_gears(self, gears_by_line: dict[int, list[Gear]]) -> bool:
        lines_to_compare = [self.line_index]
        if self.line_index > 0:
            lines_to_compare.append(self.line_index - 1)
        if self.line_index < LAST_LINE_CHARACTER_INDEX:
            lines_to_compare.append(self.line_index + 1)

        for line_to_compare in lines_to_compare:
            if line_to_compare in gears_by_line:
                for gear in gears_by_line[line_to_compare]:
                    if self._is_index_adjacent(gear.index):
                        gear.adjacent_numbers.add(self)

    def _is_index_adjacent(self, index: int):
        check_start_index = self.start_index - 1 if self.start_index > 0 else self.start_index
        check_end_index = self.end_index + 1 if self.end_index < LAST_LINE_CHARACTER_INDEX else self.end_index
        if index >= check_start_index and index < check_end_index:
            return True
        return False


file1 = open('3_input.txt', 'r')
lines = file1.readlines()

numbers: list[Number] = []
gears_by_line: dict[int, list[Gear]] = {}

line_index = 0
for line in lines:
    for match in re.finditer(r'(\d+)|(\*)', line, re.IGNORECASE):
        matched_number, matched_gear = match.groups()
        if matched_number:
            number = Number(int(matched_number), line_index, match.start(), match.end())
            numbers.append(number)
        elif matched_gear:
            gear = Gear(match.start(), line_index)
            if line_index not in gears_by_line or gears_by_line[line_index] == None:
                gears_by_line[line_index] = [gear]
            else:
                gears_by_line[line_index].append(gear)
    line_index += 1

for number in numbers:
    number.mark_adjacent_gears(gears_by_line)

gear_ratio_sum = 0
for gears in gears_by_line.values():
    for gear in gears:
        if len(gear.adjacent_numbers) == 2:
            gear_ratio = gear.adjacent_numbers.pop().value * gear.adjacent_numbers.pop().value
            gear_ratio_sum += gear_ratio

print(gear_ratio_sum)