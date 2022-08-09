def count_down(number):
    # 재귀 함수는 반드시 종료 조건이 존재 해야 한다.
    # 종료 조건이 없으면 RecursionError 발생
    if number < 0:
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)