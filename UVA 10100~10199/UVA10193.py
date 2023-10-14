import math

pair = 1
for i in range(int(input())):
    s1 = input()
    s2 = input()
    s = int(s1, 2)
    l = int(s2, 2)
    if math.gcd(s, l) != 1:
        print(f'Pair #{pair}: All you need is love!')
    else:
        print(f'Pair #{pair}: Love is not all you need!')
    pair += 1
