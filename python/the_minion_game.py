def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]

    stuart_score = 0
    kevin_score = 0
    for index in range(len(string)):
        if string[index] in vowels:
            kevin_score += (len(string) - index)
        else:
            stuart_score += (len(string) - index)

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")
