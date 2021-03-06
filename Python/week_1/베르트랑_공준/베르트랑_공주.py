# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.

# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 입력
# 1 ≤ n ≤ 123,456

# 처리
# 

# 출력
# n < result <= 2n

def find_prime_num () :
  while 1 :
    num = input()
    num = int(num)
    if num == 0 :
      break
    prime_num_list = []
    n = 2 * num
    n += 1                            # for문 사용을 위한 n += 1
    prime = [True] * (n)                # n개의 [True]가 있는 리스트 생성
    for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
      if prime[i]:                    # prime[i]가 True일때
        for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
          prime[j] = False

    for i in range(num + 1, n):
      if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
        prime_num_list.append(i)
        
    print(len(prime_num_list))

find_prime_num()