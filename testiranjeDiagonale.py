board = [
    ["a", "b", "c","d"],
    ["e", "f", "g","h"],
    ["i", "j", "k","l"],
    ["m", "n", "o","p"]
]

b = [
    ['  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ']
]

def isOver(board):
    #horizontalno preverjanje konca igre
    for el in board:
        if len(set(el))==1 and "  " not in set(el):
            return True
    #vertikalno preverjanje igre
    for i in range(len(board)):
        a = set()
        for el in board:
            a.add(el[i])
        if len(a)==1 and "  " not in a:
            return True
    #diagonalno preverjanje igre
    if len(set([r[i] for i, r in enumerate(board)]))==1 and "  " not in set([r[i] for i, r in enumerate(board)]) or len(set([r[-i-1] for i, r in enumerate(board)]))==1 and "  " not in set([r[-i-1] for i, r in enumerate(board)]):
        return True
    return False
