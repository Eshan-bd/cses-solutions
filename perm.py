from collections import deque
import sys
sys.setrecursionlimit(1000000)  # Set a higher recursion limit


n = int(input())
arr = [i for i in range(1, n+1)]
chosen = [False]*n
perm = deque()

def search():
    if len(perm)>=n:
        if is_beautiful(perm):
            print(' '.join(map(str, perm)))
            raise SystemExit
        else:
            return

    for i in range(n):
        if chosen[i]:
            continue
        chosen[i]=True
        perm.append(arr[i])
        search()
        chosen[i]=False
        perm.pop()

def is_beautiful(perm):
    for i in range(1, len(perm)):
        if abs(perm[i-1]-perm[i]) == 1:
            return False
    return True

if __name__=='__main__':
    search()
    print("NO SOLUTION")
