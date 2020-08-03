#I am testing some classes glhf

class idk:
    def __init__(self):
        self.board = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]
        
    def izpis(self):
        print(self.board)

    def spremeni(self):
        vnos = input('Vnesite kordinato')
        vnos = vnos.split()
        self.board[int(vnos[0])][int(vnos[1])] = 1
    
        

yes = idk()
yes.spremeni()
yes.izpis()
