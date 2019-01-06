class Player:
    def __init__(self, name, canvas, width, height, start):
        canvas_height = int(canvas['height'])
        canvas_width = int(canvas['width'])
        self.tag = None
        self.move = 20

        if start <= 0:
            self.x_start = 20
            self.tag = "player"
            self.move = self.move
        else:
            self.tag = "player2"
            self.x_start = canvas_width - 40
            self.move = self.move 

        # Init pos
        self.top = self.x_start
        self.left = canvas_height / 2 - height / 2
        self.bot = self.x_start + width
        self.right = canvas_height / 2 + height / 2
        self.player = canvas.create_rectangle(
            self.top, self.left, self.bot, self.right, fill='white', tags=self.tag)
        self.canvas = canvas
        self.name = name

    # Movement
    def up(self, event):
        coords = self.givePosition()
        if coords[1] <= 0:
            return 0
        self.canvas.move(self.player, 0, -self.move)

    def down(self, event):
        coords = self.givePosition()
        if coords[3] >= int(self.canvas['height']):
            return 0
        self.canvas.move(self.player, 0, self.move)

    def givePosition(self):
        return self.canvas.coords(self.player)

    def speed(self, newSpeed=20):
        self.move = newSpeed

    def resize(self, pourcentage):
        coords = self.canvas.coords(self.player)
        self.canvas.delete(self.player)
        if pourcentage == 0:
            self.player = self.canvas.create_rectangle(
                coords[0]+1, coords[1],
                coords[2], coords[1] + 100, fill="white")
        else:
            self.player = self.canvas.create_rectangle(
                coords[0], coords[1] + (pourcentage * 100),
                coords[2], coords[3] - (pourcentage * 100), fill="white")