count = 0
def search(y):
    global count
    if y==n:
        count+=1
    for x in range(n):
        if col[x] or pos_diag[x + y] or neg_diag[x - y + n - 1]:
            continue
        col[x] = pos_diag[x+y] = neg_diag[x-y+n-1] = True
        search(y+1)
        col[x] = pos_diag[x+y] = neg_diag[x-y+n-1] = False

if __name__=='__main__':
    n = int(input())
    col = [0]*n
    pos_diag = [0] * n
    neg_diag = [0] * n
    search(0)
    print(count)