def two_sets(n):
    total = n*(n+1)//2
    if total%2!=0:
        print('NO')
        return
    else:
        print('YES')

    set1 = []
    set2 = []
    remaining_sum = total//2
    set1_sum = 0
    visited = [0] * (n+1)
    max_elem = n
    while set1_sum < total//2:
        if remaining_sum > max_elem:
            set1.append(max_elem)
            set1_sum += max_elem
            visited[max_elem] = 1
            remaining_sum -= max_elem
            max_elem -= 1
        else:
            set1.append(remaining_sum)
            set1_sum += remaining_sum
            visited[remaining_sum] = 1


    for i in range(1, len(visited)):
        if visited[i] == 0:
            set2.append(i)

    print(len(set1))
    print(' '.join(map(str, [i for i in set1])))
    print(len(set2))
    print(' '.join(map(str, [i for i in set2])))

if __name__=='__main__':
    n = int(input())
    two_sets(n)