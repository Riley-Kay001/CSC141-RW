import pygame
import sys
import random


class Raindrop:
    __slots__ = ("x", "y", "speed")

    def __init__(self, x):
        self.x = x
        self.y = 0
        self.speed = random.randint(5, 10)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.line(
            screen,
            (180, 180, 255),
            (self.x, self.y),
            (self.x, self.y + 6),
            1
        )


class RaindropsManager:
    RAIN_RATE = 20

    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600
        self.bg_color = (20, 20, 30)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Rain on Full Slanted Glass")

        self.clock = pygame.time.Clock()
        self.raindrops = []

        self.last_drop_time = pygame.time.get_ticks()
        self.running = True

        self.glass_start = (0, 0)
        self.glass_end = (self.width, self.height)

    def glass_y_at(self, x):
        x1, y1 = self.glass_start
        x2, y2 = self.glass_end

        t = (x - x1) / (x2 - x1)
        return y1 + t * (y2 - y1)

    def hit_glass(self, drop):
        if drop.x < 0 or drop.x > self.width:
            return False

        glass_y = self.glass_y_at(drop.x)
        return drop.y >= glass_y

    def run(self):
        while self.running:
            self._check_events()
            self._update()
            self._draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_drop_time >= RaindropsManager.RAIN_RATE:
            x = random.randint(0, self.width)
            self.raindrops.append(Raindrop(x))
            self.last_drop_time = current_time

        for drop in self.raindrops:
            drop.update()

        self.raindrops = [
            drop for drop in self.raindrops
            if not self.hit_glass(drop)
        ]

    def _draw(self):
        self.screen.fill(self.bg_color)

        pygame.draw.line(
            self.screen,
            (80, 80, 120),
            self.glass_start,
            self.glass_end,
            4
        )

        for drop in self.raindrops:
            drop.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    manager = RaindropsManager()
    manager.run()