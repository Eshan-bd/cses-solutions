def safe_positions(k):
    total_pos = (k*k * (k*k-1)) // 2
    attacking_pos = 4 * (k-1) * (k-2)

    return total_pos - attacking_pos

if __name__=='__main__':
    for k in range(1, int(input())+1):
        print(safe_positions(k))