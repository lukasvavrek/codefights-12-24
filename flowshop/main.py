#!/usr/bin/env python

N, M = map(int, input().split())

result = []

for i in range(N):
    items = list(map(int, input().split()))
     
    for j in range(M):
        if j == 0 and i == 0:
            continue
        else:
            if i == 0:
                items[j] += items[j-1]
            else:
                if j == 0:
                    items[j] += result[i-1][j]
                else:
                    print(f'item={items[j]} a={result[i-1][j-1],}, b={items[j-1]}')
                    items[j] += max(result[i-1][j], items[j-1])

    result.append(items)

print(result)
print('==============')
print(' '.join(map(str, [x[-1] for x in result])))
