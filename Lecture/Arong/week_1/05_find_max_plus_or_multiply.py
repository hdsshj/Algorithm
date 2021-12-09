input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 현재 계산하고있는 합계를 정의
    multiply_sum = 0
    for number in array:
        # 현재 더해야하는 sum도(multiply_sum) 처음엔 0이라 고려해야 함
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)