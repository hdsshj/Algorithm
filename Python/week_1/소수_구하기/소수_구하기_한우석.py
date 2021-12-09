# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제
# 3 16

# 출력
# 3
# 5
# 7
# 11
# 13

# 입력
# 1 <= M <= N <= 1,000,000 의 자연수

# 처리
# M <= prime_num <= N
# 에라토스테네스의 체 사용
# 일정 범위내 수열에서 배수들을 제거해 소수만 남기는 방법


# 출력
# 한 줄에 하나씩, 작은 순서로 소수 출력

m, n = map(int,input().split())

def find_prime_num (m,n) :
  n += 1                            # for문 사용을 위한 n += 1
  prime = [True] * n                # n개의 [True]가 있는 리스트 생성
  for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
    if prime[i]:                    # prime[i]가 True일때
      for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)

find_prime_num(m, n)