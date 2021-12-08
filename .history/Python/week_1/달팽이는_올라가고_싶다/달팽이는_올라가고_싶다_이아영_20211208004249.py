snail = int(input())

a, b, v = map(int, input().split())

move = (v - b) // (a - b)
date = (v - b) % (a - b)

if date > 0:
    print(move + 2)
else:
    print(move + 1)
