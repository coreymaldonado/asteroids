from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, "white", (self.x, self.y),
                           self.radius, width=2)

    def update(self, dt):
        self.y + (self.velocity * dt)
