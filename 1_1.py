def find_first_number_forward(line_chars: str) -> int | None:
    for char in line_chars:
        if char.isnumeric():
            return char
    return None

def find_first_number_backward(line_chars: str) -> int | None:
    for char in line_chars[::-1]:
        if char.isnumeric():
            return char
    return None

def get_line_number_pair(line_chars: str) -> int:
    first_digit = find_first_number_forward(line_chars)
    if first_digit == None:
        return 0
    second_digit = find_first_number_backward(line_chars)
    print("first_digit", first_digit, "second_digit", second_digit)
    return int(str(first_digit) + str(second_digit))


file1 = open('1_input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    line_number_pair = get_line_number_pair(line)
    sum += line_number_pair

print(sum)