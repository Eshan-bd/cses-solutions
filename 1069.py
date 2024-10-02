s = input()

count = 1
high = 1
prev = None
for c in s:
    if c == prev:
        count+=1
    else:
        high = max(count, high)
        count=1
        prev = c
print(max(high, count))
