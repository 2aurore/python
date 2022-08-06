input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                      "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    max_occurrence = 0
    max_alpha = alphabet_array[0]

    for alpha in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alpha:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alpha = alpha

    return max_alpha


result = find_max_occurred_alphabet(input)
print(result)