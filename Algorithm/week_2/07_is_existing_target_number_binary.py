finding_target = 1
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 이진 탐색을 하기 위해서는 반드시 리스트가 정렬이 되어있어야 한다!
def is_exist_target_number_binary(target, numbers):
    current_min = 0
    current_max = len(numbers) - 1
    current_guess = (current_min + current_max) // 2

    find_count = 0
    while current_min <= current_max:
        find_count += 1
        if numbers[current_guess] == target:
            print(find_count)
            return True
        elif numbers[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
