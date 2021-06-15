# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
shoe_list = list(map(int, input().split()))
c = Counter(shoe_list)
N = int(input())
sum = 0
for i in range(N):
    size, money = map(int, input().split())
    if size in c.keys() and c[size] != 0:
        sum += money
        c[size] -= 1
print(sum)    