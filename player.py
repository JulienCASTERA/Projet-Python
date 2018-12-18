class Player:
    def __init__(self, name, canvas, width, height, start):
        canvas_height = int(canvas['height'])
        canvas_width = int(canvas['width'])
        if start <= 0:
            self.x_start = 20
        else:
            self.x_start = canvas_width - 40

        # Init pos
        self.top = self.x_start
        self.left = canvas_height / 2 - height / 2
        self.bot = self.x_start + width
        self.right = canvas_height / 2 + height / 2

        self.player = canvas.create_rectangle(
            self.top, self.left, self.bot, self.right, fill='white')
        self.canvas = canvas

        self.name = name

    # Movement
    def up(self, event):
        coords = self.givePosition()
        if coords[1] <= 0:
            return 0
        self.canvas.move(self.player, 0, -20)

    def down(self, event):
        coords = self.givePosition()
        if coords[3] >= int(self.canvas['height']):
            return 0
        self.canvas.move(self.player, 0, 20)

    def givePosition(self):
        return self.canvas.coords(self.player)
