# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,n = map(str, input().split())
n = int(n)
li = list(s)
ans_li = []
for tup in list(permutations(li,n)):
    ans_li.append(''.join(tup))
for ans in (sorted(ans_li)):
    print(ans)