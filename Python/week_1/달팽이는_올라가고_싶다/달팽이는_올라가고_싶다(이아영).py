# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
# 높이 V, 낮 +A, 밤 -B
# A, B, V
# 2 1 5
# 5 - (2 - 1) = 4
# 4 - (2 - 1) = 3
# 3 - (2 - 1) = 2
# 2 - 2 = 0

A,B,V = input().split()
A = int(A)
B = int(B)
V = int(V)

def finish_day_count(A, B, V) :
  finish_day = 0
  while 1:
    if V - A > 0 :
      V = V - (A-B)
    #   print(V-(A-B))
      finish_day += 1
    elif V - A <= 0 : 
      finish_day += 1
      break
  print(finish_day)
  
finish_day_count(A, B, V)