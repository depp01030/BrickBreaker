class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce(self):
        self.speed_y = -self.speed_y

    def reset_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision_with_paddle(self, paddle):
        if (self.x + self.radius > paddle.x and
            self.x - self.radius < paddle.x + paddle.width and
            self.y + self.radius >= paddle.y):
            self.bounce()

    def check_collision_with_brick(self, brick):
        if (self.x + self.radius > brick.x and
            self.x - self.radius < brick.x + brick.width and
            self.y - self.radius < brick.y + brick.height and
            self.y + self.radius > brick.y):
            self.bounce()
            brick.destroy()