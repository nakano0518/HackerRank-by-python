if __name__ == '__main__':
    nested_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        nested_list.append([name, score])
    score_list.sort()
    min_int = min(score_list)
    while min_int in score_list:
        score_list.remove(min_int)
    second_min_int = min(score_list)
    ans_names = []
    for list in nested_list:
        if list[1] == second_min_int:
            ans_names.append(list[0])
    ans_names.sort()
    for name in ans_names:
        print(name)
