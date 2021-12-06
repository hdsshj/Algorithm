input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for num in array: # array의 길이만큼 아래 연산이 실행
      if number == num: # 비교연산 1번 실행
        return True # N * 1 = N
    return False # 없을 시 False


result = is_number_exist(11, input)
print(result)