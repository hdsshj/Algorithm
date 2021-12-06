# 문자열 뒤집기 (문제) find_count_to_turn_out_to_all_zero_or_all_one
# 0과 1로만 이루어진 문자열이 주어졌을 때 , 이 문자를 모두 0,혹은 모두 1로 같게 만들어야 한다.
# 할 수 있는 행동은 연속된 하나의 숫자를 잡고 모두 뒤집는 것 이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
# "011110"


input = "011110"


# 011110
# 모두 0으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_zero
# 어떻게 하면 증가될까? 1111을 뒤집어야한다.
# 0 -> 1로 문자열이 전환되는 순간 count_to_all_zero += 1

# 모두 1으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_one
# 1 -> 0로 문자열이 전환되는 순간 count_to_all_one += 1

# 1) 문자열이 뒤집어질때, 즉 0 에서 1 혹은 1에서 0으로 바뀔 때  숫자들이 카운팅 되어야 함.
# 2) 첫 번째 원소가 0 인지 1인지에 따라서 숫자를 추가해줘야함


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0  # 밑에 안한거 = 첫번째 문자의 여부에 따라 zero 와 one 을 증가 시켜줘야한다. 아래추가작성

    if string[0] == '0':        # 만약에 맨 처음 문자가 0 이냐 1 이냐에 따라 증가를 해줘야한다. / 0번째의 원소가 0 이라면
        count_to_all_one += 1   # one 을 하나 더 증가
    elif string[0] == '1':      # 그게아니라 1이라면
        count_to_all_zero += 1  # 반대로 zero 를 증가 시켜준다.

    for i in range(len(string) - 1):     # 이때 앞뒤의 문자들을 봐야하기 때문에 i를 index 로 사용
        if string[i] != string[i + 1]:   # 1 -> 0 0 -> 1 / i번째 문자가 i+1 문자와 다르다는 소리
            if string[i + 1] == '0':     # 다음문자가 0 이라면
                count_to_all_one += 1    # 하나씩 증가 왜냐? 1 -> 0 으로 변환되었단 소리는 앞에 있는 숫자들을 전부 0 으로 변환시켜 줘야한다. 라고 생각
            if string[i + 1] == '1':     # 다음문자가 1 이라면
                count_to_all_zero += 1   # 제로를 하나더 증가 이 과정에서 안한게 있음.
    # print(count_to_all_one, count_to_all_zero)
    return min(count_to_all_one, count_to_all_zero)  # 최소값을 주는 방법 (넣어진 인자 중에서 가장 최소값)
    # return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 결과 2 1  print(count_to_all_one, count_to_all_zero)
#  1
# one 은 모두 1로 만들기 위한 최소 뒤집는 숫자는 2번 모두 0 으로 만들기 위한 최소 숫자는 1 번


# 특정규칙을 스스로 발견해서 어떻게 코드화 할건지 구현하는 문제
