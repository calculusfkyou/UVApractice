def main():
    max_len = 0
    sentences = []
    while True:
        try:
            s = input()
            sentences.append(s)
            if max_len < len(s):
                max_len = len(s)
        except EOFError:
            break
    for i in range(len(sentences)):
        for j in range(max_len - len(sentences[i])):
            sentences[i] += " "
    sentences.reverse()
    for i in range(max_len):
        for j in range(len(sentences)):
            print(sentences[j][i], end="")
        print()


if __name__ == "__main__":
    main()
