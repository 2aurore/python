input = "111010"

# 모두 0으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_zero
# 0 -> 1로 문자열이 전환되는 순간에 해당 변수를 +1

# 모두 1으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_one
# 0 -> 1로 문자열이 전환되는 순간에 해당 변수를 +1

# 1) 문자열이 뒤집어질 때, 0->1, 1->0으로 바뀔때
# 2) 첫번째 원소가 0인지, 1인지에 따라 숫자를 추가해야 함

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1   # 첫번째 문자가 0일 때, 1로 전환하는 count +1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:  # 앞 뒤 문자열이 0과 1로 서로 다름
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    print(count_to_all_one, count_to_all_zero)
    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)