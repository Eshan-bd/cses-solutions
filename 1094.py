def main():
    n = int(input())
    arr = list(map(int, input().split()))
    if n<=1:
        print(0)
        return

    moves = 0
    for i in range(1, n):
        diff = arr[i-1]-arr[i]
        if diff>0:
            moves += diff
            arr[i] = arr[i-1]
    print(moves)

if __name__=='__main__':
    main()
