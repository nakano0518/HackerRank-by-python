from collections import OrderedDict
def merge_the_tools(s, k):
    # your code goes here
    li = []
    for i in range(0, len(s), k):
        if i+k > len(s):
            li.append(s[i: len(s)])
        else: 
            li.append(s[i: i+k])
    for string in li:
        print(''.join(OrderedDict.fromkeys(string)))