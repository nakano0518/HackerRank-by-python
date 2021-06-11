# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
center = n//2+1
for i in range(center-1):
    c = '.|.'
    pat = c*(2*i+1)
    print(pat.center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(center-1):
    c = '.|.'
    pat = c*(2*(center-2-i)+1)
    print(pat.center(m, '-'))