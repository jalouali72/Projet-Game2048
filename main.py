def __init__(self):
    self.n = 4
    self.window = Tk()
    self.window.title('ProjectGurukul 2048 Game')
    self.gameArea = Frame(self.window, bg='azure3')
    self.board = []
    self.gridCell = [[0] * 4 for i in range(4)]
    self.compress = False
    self.merge = False
    self.moved = False
    self.score = 0
    for i in range(4):
        rows = []
        for j in range(4):
            l = Label(self.gameArea, text='', bg='azure4',
                      font=('arial', 22, 'bold'), width=4, height=2)
            l.grid(row=i, column=j, padx=7, pady=7)
            rows.append(l);
        self.board.append(rows)
    self.gameArea.grid()




