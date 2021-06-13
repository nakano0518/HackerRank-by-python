def minion_game(s):
    # your code goes here
    vowels = 'AEIOU'

    k_sc = 0
    s_sc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            k_sc += (len(s)-i)
        else:
            s_sc += (len(s)-i)

    if k_sc > s_sc:
        print("Kevin", k_sc)
    elif k_sc < s_sc:
        print("Stuart", s_sc)
    else:
        print("Draw")
            
