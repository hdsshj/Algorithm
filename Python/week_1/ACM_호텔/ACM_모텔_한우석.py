# 방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다. 
# 즉, 그림 1 에서 빗금으로 표시한 방은 305 호가 된다.
# 손님은 엘리베이터를 타고 이동하는 거리는 신경 쓰지 않는다. 
# 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다. 예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 
# 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다. 같은 이유로 102 호보다 2101 호를 더 선호한다.
# 여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 
# 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 
# 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.

# 입력
# 프로그램은 표준 입력에서 입력 데이터를 받는다. 
# 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 
# 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다
# (1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).
# t 반복 횟수, h 층수, w 방수, n 몇 번째 손님

# 출력
# 프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

t = input()
t = int(t)
#  h 층수, w 방수, n 몇 번째 손님
for num in range(t) :
  h,w,n = map(int,input().split())
  num = n//h + 1
  floor = n % h
  if n % h == 0:  # h의 배수이면,
      num = n//h
      floor = h
  print(f'{floor*100+num}')
    