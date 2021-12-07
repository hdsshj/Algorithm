input = 20


# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다. 0과1은 소수가 아니다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하
def find_prime_list_under_number(number):
    prime = []
    # range함수는 number+1에서 하나를 뺀 숫자인 number까지 반복
    for i in range(2, number + 1):  # i의 범위 : 2부터 number까지
        # 소수인지 아닌지 파악하기 위해 반복문 다시 돌림(i가 소수인지 아닌지 판별)
        # for j in range(2, i):  j의 범위 : 2부터 n-1까지
        for j in prime:  # j의 범위 : 2부터 n-1까지의 소수 (모든 숫자가 아닌 n-1까지의 소수만 돌려서 연산량이 줄어듦)
            if i % j == 0 and j * j <= i:
                break
        #  break를 타지 않았다면 소수이기 때문에 prime에 추가해준다.
        else:
            prime.append(i)

    return prime


result = find_prime_list_under_number(input)
print(result)