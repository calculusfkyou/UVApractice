# WA not yet
from itertools import permutations


def main():
    T = int(input())

    for _ in range(T):
        s = input().strip()
        sorted_s = ''.join(sorted(s))

        perms = permutations(sorted_s)
        for perm in perms:
            print(''.join(perm))

        print()


if __name__ == "__main__":
    main()
