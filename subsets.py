q = []
def search(k):
    if k>n:
        print(q)
    else:
        q.append(k)
        search(k+1)
        q.pop()
        search(k+1)

if __name__=='__main__':
    n = int(input())
    search(1)