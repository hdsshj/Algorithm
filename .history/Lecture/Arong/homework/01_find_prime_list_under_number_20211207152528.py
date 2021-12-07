input = 20


def find_prime_list_under_number(number):
    prime = []
    for i in range(2, number + 1):
        cnt = 0
        for j in range(2, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            prime.append(i)

    return prime


result = find_prime_list_under_number(input)
print(result)