def get_number(x, y):
    if y<=x:
        start = (y-1) * (y-1)
        if y%2==0:
            #     print(start + y)
            # else:
            #     print(start + 2*y-x)
        else:
            if x<=y:
                print(start + x)
            else:
                print(2*x-y)



if __name__=='__main__':
    y, x = list(map(int, input().split()))
    get_number(x, y)