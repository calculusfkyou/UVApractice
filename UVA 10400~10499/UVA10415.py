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
t = int(input())
for i in range(t):
    case = input()
    state = [0] * 11  # 現在是否按下的狀態 #不管第0個
    num = [0] * 11  # 最後把第0個pop
    for j in range(len(case)):
        t = case[j]
        for k in range(len(finger)):
            if finger[k][0] == t:
                temp = k  #
        for k in range(1, len(state)):
            if state[k] == 0 and finger[temp][k] == 1:
                num[k] += 1
                state[k] = 1
            if finger[temp][k] == 0:
                state[k] = 0
    num.pop(0)
    print(*num)
