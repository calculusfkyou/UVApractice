def main():
    while True:
        try:
            n = int(input())
            blocks=[[i]for i in range(n)]
            while True:
                movement=input()
                if movement=="quit":
                    break
                movement=movement.split()
                if movement[0]==movement[2]:
                    break
                t1,t2=int(movement[1]),int(movement[-1])
                if movement[0]+movement[2]=="moveonto":
                    
                elif movement[0]+movement[2]=="pileonto":

                elif movement[0]+movement[2]=="pileover":

            for i in range(len(blocks)):
                print("%d: "%(i),end="")
                print(*blocks[i])
        except EOFError:
            break

if __name__ == "__main__":
    main()