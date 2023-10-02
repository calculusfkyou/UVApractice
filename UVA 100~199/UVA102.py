def main():
    while True:
        try:
            b1, g1, c1, b2, g2, c2, b3, g3, c3 = map(int, input().split())
            move = [0] * 6
            move[0] = b2 + b3 + g1 + g2 + c1 + c3
            move[1] = b2 + b3 + g1 + g3 + c1 + c2
            move[2] = b1 + b3 + g1 + g2 + c2 + c3
            move[3] = b1 + b2 + g1 + g3 + c2 + c3
            move[4] = b1 + b3 + g2 + g3 + c1 + c2
            move[5] = b1 + b2 + g2 + g3 + c1 + c3
            minIndex = 0
            for i in range(1, 6):
                if move[i] < move[minIndex]:
                    minIndex = i
            ANSWERS = ["BCG", "BGC", "CBG", "CGB", "GBC", "GCB"]
            print(f"{ANSWERS[minIndex]} {move[minIndex]}")
        except EOFError:
            break


if __name__ == "__main__":
    main()
