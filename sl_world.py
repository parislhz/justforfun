import sys
import pygame
from pygame.locals import *
import math

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
PLANET_X = 512
PLANET_Y = 1000
# PLANET_Y = 768
PLANET_R = 512
BACKGROUND_COLOR = (255, 255, 255)


class PlanetObject(pygame.sprite.Sprite):
    def __init__(self, angle, r, size, img_path):
        super(PlanetObject, self).__init__()
        self.angle = angle
        self.r = r
        self.size = size
        self.planet_angle = 0
        self.img_path = img_path
        self.calc_abs_pos()

    def calc_abs_pos(self):
        theta = self.angle - self.planet_angle
        surf = pygame.image.load(self.img_path)
        surf = pygame.transform.scale(surf, self.size)
        self.surf = pygame.transform.rotate(surf, -theta * 180 / math.pi)
        x = PLANET_X + PLANET_R * math.sin(theta)
        y = PLANET_Y - PLANET_R * math.cos(theta)
        self.rect = self.surf.get_rect(center=(x, y))

    def update(self, planet_angle):
        self.planet_angle = planet_angle
        self.calc_abs_pos()


class SunsetLightess:
    pygame.init()
    pygame.display.set_caption('MAZE')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self):
        self.planet_angle = 0
        self.planet_objects = pygame.sprite.Group()
        obj = PlanetObject(0, 512, (64, 64), 'res/Belt_2.png')
        self.planet_objects.add(obj)
        obj = PlanetObject(10 * math.pi / 180, 650, (64, 32), 'res/Hood_2.png')
        self.planet_objects.add(obj)
        obj = PlanetObject(-20 * math.pi / 180, 450, (32, 64), 'res/Sword2.png')
        self.planet_objects.add(obj)

    def run_game(self):
        while True:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_a:
                        self.planet_angle = self.planet_angle - 2 * math.pi / 180
                    elif event.key == K_d:
                        self.planet_angle = self.planet_angle + 2 * math.pi / 180

            self.screen.fill(BACKGROUND_COLOR)
            for obj in self.planet_objects:
                obj.update(self.planet_angle)
                self.screen.blit(obj.surf, obj.rect)
            pygame.display.flip()


def main():
    game = SunsetLightess()
    game.run_game()


if __name__ == '__main__':
    main()
