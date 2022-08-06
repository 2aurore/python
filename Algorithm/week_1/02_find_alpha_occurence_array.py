input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurred_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        char_num = ord(char) - ord('a')
        alphabet_occurred_array[char_num] += 1

    return alphabet_occurred_array


result = find_max_occurred_alphabet(input)
print(result)