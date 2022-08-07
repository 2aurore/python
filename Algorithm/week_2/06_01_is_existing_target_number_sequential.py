finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    # 이진 탐색과의 시간복잡도 비교를 위한 변수
    find_count = 0
    for number in array:
        find_count += 1
        if target == number:
            print(find_count)
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True