from random import randint

class Bonus(object):
    def __init__(self, canvas, player, player2, ball):
        self.pos_x = randint(100, int(canvas['width'])-100)
        self.pos_y = randint(20, int(canvas['height'])-20)
        self.canvas = canvas
        self.ball = ball
        self.bon = None
        col = randint(0, 4)
        if col == 0:
            self.color = 'red'
        elif col == 1:
            self.color = 'blue'
        elif col == 2:
            self.color = 'yellow'
        elif col == 3:
            self.color = 'green'
        else:
            self.color = 'purple'

        self.initiation()


    def initiation(self):
        self.bonus = self.canvas.create_oval(self.pos_x, self.pos_y, self.pos_x+55, self.pos_y+55, fill=self.color, tags="bon")

        
    def checkCol(self, balle, player, player2):
        if self.canvas.find_overlapping(self.pos_x,self.pos_y, self.pos_x+55, self.pos_y+55) != (self.bonus, ):
            self.canvas.delete("bon")
            return self.color
        else:
            return None
