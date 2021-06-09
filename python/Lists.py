def do_command(ans_li, command_li):
    if command_li[0] == 'insert':
        ans_li.insert(int(command_li[1]), int(command_li[2]))
    elif command_li[0] == 'print':
        print(ans_li)
    elif command_li[0] == 'remove':
        ans_li.remove(int(command_li[1]))
    elif command_li[0] == 'append':
        ans_li.append(int(command_li[1]))
    elif command_li[0] == 'sort':
        ans_li.sort()
    elif command_li[0] == 'pop':
        ans_li.pop()
    elif command_li[0] == 'reverse':
        ans_li.reverse()
if __name__ == '__main__':
    n = int(input())
    command_lists = [list(map(str, input().split())) for _ in range(n)]
    #print(command_li)
    ans_li = []
    for command_li in command_lists:
        do_command(ans_li, command_li)
