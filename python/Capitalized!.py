# Complete the solve function below.
def solve(s):
    li = list(s.split(' '))
    for i, s in enumerate(li):
        li[i] = s.capitalize()
    return ' '.join(li)