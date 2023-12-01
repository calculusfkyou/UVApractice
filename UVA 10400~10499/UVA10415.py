finger = [["c", 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
          ["d", 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
          ["e", 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
          ["f", 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
          ["g", 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
          ["a", 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          ["b", 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          ["C", 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          ["D", 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
          ["E", 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
          ["F", 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
          ["G", 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
          ["A", 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          ["B", 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
n = int(input())
for i in range(n):
    count, current = [0 for j in range(10)], [0 for j in range(10)]
    st = input()
    for j in range(len(st)):
        temp = ""
        for k in range(len(finger)):
            if finger[k][0] == st[j]:
                temp = finger[k][1:]
                break
        for k in range(10):
            if (current[k] != temp[k]) & temp[k] == 1:
                count[k] += 1
        current = temp
    print(*count)
