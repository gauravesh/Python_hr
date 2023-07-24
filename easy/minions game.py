def minion_game(string):

    ls_string = list(string)

    # Minions game
    cons = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vowels = ['A', 'E', 'I', 'O', 'U']

    # Initialize scores for Stuart and Kevin
    stuart_score = 0
    kevin_score = 0
    stuart_substrings = []
    kevin_substrings = []

    for index_i, i in enumerate(ls_string):
        if i in cons:
            for index_j in range(index_i+1, len(ls_string)+1):
                substring = ''.join(ls_string[index_i:index_j])
                if substring not in stuart_substrings:
                    stuart_substrings.append(substring)
                    stuart_score += 1
                else:
                    stuart_score = stuart_score+1
        elif i in vowels:
            for index_j in range(index_i+1, len(ls_string)+1):
                substring = ''.join(ls_string[index_i:index_j])
                if substring not in kevin_substrings:
                    kevin_substrings.append(substring)
                    kevin_score += 1
                else:
                    kevin_score=kevin_score+1

    # Determine the winner
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")
