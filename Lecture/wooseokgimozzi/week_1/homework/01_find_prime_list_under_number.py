input = 20


def find_prime_list_under_number(number):
    prime_list=[]
    for num in range(2, number+1): # num은 2 ~ 20
        # for i in range(2,num): # i 를 num-1까지 나눔
        for i in prime_list : # prime_list는 소수의 리스트, num이 2일땐 prime_list가 없기 때문에 타지 않는다.
            if num%i == 0 and i * i <= num:
                break
        else:
            prime_list.append(num)
    return prime_list

result = find_prime_list_under_number(input)
print(result)