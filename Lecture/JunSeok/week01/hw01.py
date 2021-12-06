# 소수 나열하기 (문제) find_prime_list_under_number
# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수없는 1보다 큰 자연수이다.
# 20 이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

input = 20


# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은 N 이 N의 제곱근 보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는 반드시 N의 제곱근 이하


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):  # n의 범위는 2부터 number 까지
        # n 이 20 이라고 한다면
        # i 를 2 3 5 7 9 .. 19
        # 2 ~ n - 1 중에서 소수인 애들만

        # for i in range(2, n):     # 소수인지 아닌지 파악한다. i의 범위는 2부터 n - 1 까지
        for i in prime_list:  # i의 범위는 2부터 n - 1 까지의 소수
            # if n % i == 0:        # 나누어 떨어진다면
            if n % i == 0 and i * i <= n:  # 제곱근까지만 나누어 질수 있기 때문에 조건을 걸어줬음 2,3,5 까지만 소수인지 비교 하면 되기 때문
                break
        else:  # 브레이크 안걸리면
            prime_list.append(n)  # 이 숫자를 프라밈리스트에 추가
    return prime_list  # 이 방법은 효율적이지 못함


result = find_prime_list_under_number(input)
print(result)

# 알고리즘은 어떤식으로든 개선할 수 있다.
# 수학적 특징 혹은 특정 숫자의 특징이나 개념들을 떠올리면 힌트를 얻기 더 쉽다.
