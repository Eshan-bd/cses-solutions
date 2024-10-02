# from collections import deque
# import sys
# sys.setrecursionlimit(1000000)  # Set a higher recursion limit


n = int(input())
res_odd = []
res_even = []
def perm():
    for i in range(1, n+1):
        if i%2==0:
            res_even.append(i)
        else:
            res_odd.append(i)


if __name__=='__main__':
    if n in [2, 3]:
        print("NO SOLUTION")
    else:
        perm()
        print(' '.join(map(str, res_even+res_odd)))
