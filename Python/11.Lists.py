if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        cmd, *line = input().split()
        #print('list.{:}{:}'.format(cmd,tuple(map(int,line))))
        if cmd != "print":
            eval('list.{:}{:}'.format(cmd,tuple(map(int,line))))
        elif cmd == "print":
            print(list)
