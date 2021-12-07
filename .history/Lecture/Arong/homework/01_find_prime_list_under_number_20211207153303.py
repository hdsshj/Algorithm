input = 20


# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다. 0과1은 소수가 아니다.
def find_prime_list_under_number(number):
    prime = []
    # range함수는 number+1에서 하나를 뺀 숫자인 number까지 반복
    for i in range(2, number + 1):
        # 소수인지 아닌지 파악하기 위해 반복문 다시 돌림(i가 소수인지 아닌지 판별)
        for j in range(2, i):
            if i % j == 0:
                break
        #  break를 타지 않았다면 소수이기 때문에 prime에 추가해준다.
        else:
            prime.append(i)

    return prime


result = find_prime_list_under_number(input)
print(result)