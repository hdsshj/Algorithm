a, b, v = map(int, input().split())

move_date = (v - a) // (a - b)
date = (v - a) % (a - b)

if date > 0:
    print(move_date + 2)
else:
    print(move_date + 1)
