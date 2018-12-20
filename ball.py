class Ball:
    def __init__(self, canvas, radius, vitesse):
        self.canvas = canvas
        canvas_height = int(canvas['height'])
        canvas_width = int(canvas['width'])
        self.radius = radius
        # Init pos
        self.x1 = canvas_width / 2 - self.radius / 2
        self.y1 = canvas_height / 2 - self.radius / 2
        self.x2 = canvas_width / 2 + self.radius / 2
        self.y2 = canvas_height / 2 + self.radius / 2
        self.ball = self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill='white')
        self.x_speed = vitesse
        self.y_speed = vitesse
        self.move()

    def move(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        self.canvas.after(34, self.move)