n, m = map(int, input().split())
res1 = []
res2 = []
a = []

for i in range(n):
    t = list(map(int, input().split()))
    mn = min(t)
    res1.append(mn)
    a.append(t)

res1.sort()

for i in range(m):
    mx = max(a[j][i] for j in range(n))
    res2.append(mx)

res2.sort()

print(res1[-1], res2[0])
