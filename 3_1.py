import re

class Number:
    def __init__(self, value: int, line_index: int, start_index: int, end_index: int):
        self.value: int = value
        self.line_index: int = line_index
        self.start_index: int = start_index
        self.end_index: int = end_index
        #print(value, line_index, start_index, end_index)

    def is_adjacent_to_symbol(self, lines: list[str]) -> bool:
        line_self = lines[self.line_index]
        line_before = lines[self.line_index - 1] if self.line_index > 0 else None
        line_after = lines[self.line_index + 1] if self.line_index < len(lines) - 1 else None
        if self._has_line_adjacent_symbol(line_self):
            return True
        if line_before is not None and self._has_line_adjacent_symbol(line_before):
            return True
        if line_after is not None and self._has_line_adjacent_symbol(line_after):
            return True
        return False

    def _has_line_adjacent_symbol(self, line: str) -> bool:
        check_start_index = self.start_index - 1 if self.start_index > 0 else self.start_index
        check_end_index = self.end_index + 1 if self.end_index < len(line) - 1 else self.end_index

        check_index = check_start_index
        while(check_index < check_end_index):
            if self._is_symbol(line[check_index]):
                return True
            check_index += 1
        return False

    def _is_symbol(self, char: str) -> bool:
        if char.isnumeric():
            return False
        if char == ".":
            return False
        return True


file1 = open('3_input.txt', 'r')
lines = file1.readlines()

numbers: list[Number] = []
line_index: int = 0
for line in lines:
    for match in re.finditer(r'(\d+)', line, re.IGNORECASE):
        number = Number(int(match.group()), line_index, match.start(), match.end())
        numbers.append(number)
    line_index += 1

numbers_ajdacent_to_symbol_sum = 0
for number in numbers:
    if number.is_adjacent_to_symbol(lines):
        numbers_ajdacent_to_symbol_sum += number.value

print(numbers_ajdacent_to_symbol_sum)