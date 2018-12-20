from random import randint

class Bonus(object):
    def __init__(self, canvas, player, player2, ball, last):
        self.pos_x = randint(100, int(canvas['width'])-100)
        self.pos_y = randint(20, int(canvas['height'])-20)
        self.type = None
        self.canvas = canvas
        self.ball = ball
        self.last = last
        col = randint(0, 1)
        
        if col == 1:
            self.color = 'red'
        else:
            self.color = 'blue'

        self.initiation()


    def initiation(self):
        self.bonus = self.canvas.create_oval(self.pos_x, self.pos_y, self.pos_x+55, self.pos_y+55, fill=self.color, tags="bon")
        self.type = randint(0, 1)

        
    def checkCol(self):
        if self.canvas.find_overlapping(self.pos_x,self.pos_y, self.pos_x+55, self.pos_y+55) != (self.bonus, ):
            self.canvas.delete("bon")
        if self.color == 'red':
            if self.last == 'player':
                player.move = 60
      
            return 0