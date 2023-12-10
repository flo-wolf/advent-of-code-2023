number_word_values: dict[str, int] = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def find_number(line_chars: str, is_forward: bool) -> int | None:
    # populate search dict -- (number_word : character index to look at next)
    word_crawl_dict: dict[str, int] = {}
    for word in number_word_values.keys():
        # begin looking at the first/last index for each word
        word_crawl_dict[word] = 0 if is_forward else len(word) - 1

    if not is_forward:
        line_chars = line_chars[::-1]

    for line_char in line_chars:
        if line_char.isnumeric():
            return line_char

        # find number words
        for word, word_char_index in word_crawl_dict.items():
            word_start_index = 0 if is_forward else len(word) - 1
            word_end_index = len(word) - 1 if is_forward else 0

            word_char = word[word_char_index]
            start_word_char = word[word_start_index]

            if line_char == word_char:
                if word_char_index == word_end_index:
                    # the word was fully found!
                    word_crawl_dict[word] = word_start_index
                    return number_word_values[word]
                else:
                    word_crawl_dict[word] = word_char_index + 1 if is_forward else word_char_index - 1
            elif line_char == start_word_char:
                # we weren't able to continue the word, but since the first char fits, we can restart it
                word_crawl_dict[word] = word_start_index + 1 if is_forward else word_start_index - 1
            else:
                # this word doesn't fit, reset the word
                word_crawl_dict[word] = word_start_index
    return None

def get_line_numbers(line_chars: str) -> int:
    first_digit = find_number(line_chars, True)
    if first_digit == None:
        return 0
    second_digit = find_number(line_chars, False)
    return int(str(first_digit) + str(second_digit))

def accumulate_line_sums():
    file1 = open('1_input.txt', 'r')
    lines = file1.readlines()
    sum = 0
    for line in lines:
        sum += get_line_numbers(line)
    print(sum)

accumulate_line_sums()