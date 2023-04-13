"""
Question 2

gi_hun = ali = height same = K
players = N
gi hun is behind Ali nut not right behind him, there are people in between
"""

def shot(N, K, x):
    cnt = 0
    for i in x:
        if i > K:
            # x.remove(i)
            cnt += 1

    return cnt

inp = int(input())
res = []
for i in range(inp):
    N, K = map(int, input().split())
    # K = int(input())
    x = map(int, input().split(' '))
    
    res.append(shot(N,K,x))

print()

for i in res:
    print(i)






