input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurred_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        char_num = ord(char) - ord('a')
        alphabet_occurred_array[char_num] += 1
    # print(alphabet_occurred_array)

    max_occurrence = 0
    max_alpha_index = 0

    for index in range(len(alphabet_occurred_array)):
        alphabet_occurrence = alphabet_occurred_array[index]
        # print(index)

        if alphabet_occurrence > max_occurrence:
            max_alpha_index = index
            max_occurrence = alphabet_occurrence
            # print(max_alpha_index)


    return chr(max_alpha_index+ord('a'))


result = find_max_occurred_alphabet(input)
print(result)