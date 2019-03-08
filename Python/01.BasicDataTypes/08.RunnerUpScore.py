if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

sortedArr = sorted(set(arr))
print(sortedArr[-2])