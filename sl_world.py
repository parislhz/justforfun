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
BACKGROUND_COLOR = (150, 150, 100)


class PlanetObject(pygame.sprite.Sprite):
    def __init__(self, angle, r, size, img_path):
        super(PlanetObject, self).__init__()
        self.angle = angle
        self.r = r
        self.size = size
        self.planet_angle = 0
        self.img_path = img_path
        self.orig_surf = pygame.image.load(self.img_path).convert_alpha()
        self.orig_surf = pygame.transform.scale(self.orig_surf, self.size)
        self.surf = self.orig_surf
        self.rect = (0, 0, 0, 0)
        self.calc_abs_pos()

    def calc_abs_pos(self):
        theta = self.angle - self.planet_angle
        self.surf = pygame.transform.rotate(self.orig_surf, -theta * 180 / math.pi)
        x = PLANET_X + self.r * math.sin(theta)
        y = PLANET_Y - self.r * math.cos(theta)
        self.rect = self.surf.get_rect(center=(x, y))

    def update(self, planet_angle):
        self.planet_angle = planet_angle
        self.calc_abs_pos()


class Player(pygame.sprite.Sprite):
    def __init__(self, size, img_path):
        super(Player, self).__init__()
        self.size = size
        self.planet_angle = 0
        self.img_path = img_path
        self.surf = pygame.image.load(self.img_path).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, self.size)
        self.rect = self.surf.get_rect(center=(PLANET_X, PLANET_Y - PLANET_R))


class SunsetLightess:
    pygame.init()
    pygame.display.set_caption('MAZE')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self):
        self.planet_angle = 0
        self.planet_objects = pygame.sprite.Group()
        player = Player((48, 96), 'res/Bracelet_2.PNG')
        self.planet_objects.add(player)
        earth = PlanetObject(0, 0, (1000, 1000), 'res/Earth-PNG-Image.png')
        self.planet_objects.add(earth)
        obj = PlanetObject(0, 512, (64, 64), 'res/Belt_2.png')
        self.planet_objects.add(obj)
        obj = PlanetObject(10 * math.pi / 180, 650, (64, 32), 'res/Hood_2.png')
        self.planet_objects.add(obj)
        obj = PlanetObject(-20 * math.pi / 180, 550, (32, 64), 'res/Sword2.png')
        self.planet_objects.add(obj)
        obj = PlanetObject(-30 * math.pi / 180, 800, (128, 128), 'res/Hammer1_3.png')
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
