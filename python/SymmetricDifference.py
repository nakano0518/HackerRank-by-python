M = int(input())
a = set(list(map(int, input().split())))
N = int(input())
b = set(list(map(int, input().split())))

c = a.difference(b)
d = b.difference(a)
e = c.union(d)

ans = list(e)
ans.sort()
for i in range(len(ans)):
    print(ans[i])