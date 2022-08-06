input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurred_array = [0] * 26  # 각 알파벳을 인덱스 순서에 맞게 count 할 수 있는 array

    for char in string:
        if not char.isalpha():
            continue
        char_num = ord(char) - ord('a')
        alphabet_occurred_array[char_num] += 1
    # print(alphabet_occurred_array)

    not_repeating_character_array = []
    for index in range(len(alphabet_occurred_array)):
        alphabet_occurrence = alphabet_occurred_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))
    # print(not_repeating_character_array)
    # 기존 문자열의 순서를 보장하지 않고 중복되지 않은 모든 알파벳을 반환하는 array가 된다

    for char in string:
        if char in not_repeating_character_array:
            return char



result = find_not_repeating_character(input)
print(result)
