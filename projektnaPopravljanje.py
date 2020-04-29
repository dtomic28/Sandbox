import random
#initializacija programa in delovanja
rezultat = [
    ["  ", "  ", "  ","  "],
    ["  ", "  ", "  ","  "],
    ["  ", "  ", "  ","  "],
    ["  ", "  ", "  ","  "]
]

def izpis():
    tabela = ['+-1-+-2-+-3-+-4-+', 
    'a %s| %s| %s| %s|' %(rezultat[0][0],rezultat[0][1],rezultat[0][2],rezultat[0][3]),
    '+---+---+---+---+',
    'b %s| %s| %s| %s|' %(rezultat[1][0],rezultat[1][1],rezultat[1][2],rezultat[1][3]),
    '+---+---+---+---+',
    'c %s| %s| %s| %s|' %(rezultat[2][0],rezultat[2][1],rezultat[2][2],rezultat[2][3]),
    '+---+---+---+---+',
    'd %s| %s| %s| %s|' %(rezultat[3][0],rezultat[3][1],rezultat[3][2],rezultat[3][3]),
    '+---+---+---+---+']
    [print(i) for i in tabela]

def restart():
    return {
    'a':["  ", "  ", "  ","  "],
    'b':["  ", "  ", "  ","  "],
    'c':["  ", "  ", "  ","  "],
    'd':["  ", "  ", "  ","  "]
    }

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


