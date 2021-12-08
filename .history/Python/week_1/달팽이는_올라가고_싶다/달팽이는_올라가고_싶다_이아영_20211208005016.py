snail = int(input())

a, b, v = map(int, input().split())

move = (v - a) // (a - b)
date = (v - a) % (a - b)

if date > 0:
    print(move + 2)
else:
    print(move + 1)
