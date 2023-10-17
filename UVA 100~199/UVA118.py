def direction(instruction, side):
    if side == "E":
        if instruction == "R":
            return "S"
        elif instruction == "L":
            return "N"
    elif side == "W":
        if instruction == "R":
            return "N"
        elif instruction == "L":
            return "S"
    elif side == "N":
        if instruction == "R":
            return "E"
        elif instruction == "L":
            return "W"
    elif side == "S":
        if instruction == "R":
            return "W"
        elif instruction == "L":
            return "E"


x, y = map(int, input().split())
world = [[1 for i in range(x + 1)] for j in range(y + 1)]
while True:
    try:
        initialX, initialY, side = input().strip(" ").split()
        instructions = input()
        initialX = int(initialX)
        initialY = int(initialY)
        subX, subY, check, subside = 0, 0, 0, ""
        for i in range(len(instructions)):
            if instructions[i] != " ":
                subside = side
                subX = initialX
                subY = initialY
                if instructions[i] == "R" or instructions[i] == "L":
                    side = direction(instructions[i], side)
                else:
                    if side == "E":
                        initialX += 1
                    elif side == "W":
                        initialX -= 1
                    elif side == "N":
                        initialY += 1
                    elif side == "S":
                        initialY -= 1
                # print("%d %d" % (subX, subY))
                if initialX > x or initialX < 0 or initialY > y or initialY < 0:
                    if world[subY][subX] != 0:
                        world[subY][subX] = 0
                        check = 1
                        break
                    else:
                        initialX = subX
                        initialY = subY

        if check == 1:
            print("%d %d %s LOST" % (subX, subY, subside))
        else:
            print("%d %d %s" % (initialX, initialY, side))
    except EOFError:
        break
