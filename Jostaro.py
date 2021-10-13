import pygame
from pygame import *
from settings import *
from characters import *
from platformes import *
from settings import *
from pygame import mixer
from pygame.locals import *
import sys
import os
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption("GAME")
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
start_image = pygame.image.load('data/fon_start.png')
settings_image = pygame.image.load('data/afgt.png')
platforms = []
timer = pygame.time.Clock()
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group()

fiz1 = pygame.image.load('data/igri.png')
fiz2 = pygame.image.load('data/igri2.png')
fiz3 = pygame.image.load('data/igri3.png')
fiz4 = pygame.image.load('data/igri4.png')
fiz5 = pygame.image.load('data/igri5.png')
inf1 = pygame.image.load('data/inf1.png')
inf2 = pygame.image.load('data/inf2.png')
inf3 = pygame.image.load('data/inf3.png')
inf4 = pygame.image.load('data/inf4.png')
inf5 = pygame.image.load('data/inf5.png')

#видео
class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def reverse(self, pos):
        return pos[0] - self.state.left, pos[1] - self.state.top
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2
    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min(0, t)
    return Rect(l, t, w, h)
def load_level(name):
    fullname = 'levels' +'/' + name
    with open(fullname, 'r') as map_file:
        level_map = []
        for line in map_file:
            line = line.strip('/n')
            level_map.append(line)
    return level_map
font = pygame.font.SysFont(None, 20)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def settings():
    sys.exit(0)
click = False
def main_menu():
    while True:
        screen.blit(start_image,start_image.get_rect())

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(17, 43, 201, 97)
        button_2 = pygame.Rect(18, 130, 201, 185)
        button_3 =pygame.Rect(2, 590, 147, 639)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_3.collidepoint((mx, my)):
            if click:
                goodbie()
        if button_2.collidepoint((mx, my)):
            if click:
                settings()
        pygame.display.update()
def settings():
    while True:
        screen.blit(settings_image,settings_image.get_rect())
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(600, 10, 700, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
def zadaniya(imagelol,meme,uro):
    while True:
        screen.blit(imagelol,imagelol.get_rect())
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(48, 228, 195, 288)
        button_2 = pygame.Rect(572, 228, 720, 289)
        button_3 =pygame.Rect(50, 420, 197, 482)
        button_4 =pygame.Rect(572, 419, 719, 483)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button_1.collidepoint((mx, my)):
            if click:
                if meme == 5 and uro==1:
                    level2()
                if meme==4 and uro==1:
                    zadaniya(fiz5,5,1)
                if meme ==2 and uro ==2:
                    zadaniya(inf3,3,2)
        if button_2.collidepoint((mx, my)):
            if click:
                if meme ==3 and uro ==2:
                    zadaniya(inf4,4,2)

        if button_3.collidepoint((mx, my)):
            if click:
                if meme == 3 and uro ==1:
                    zadaniya(fiz4, 4,1)
        if button_4.collidepoint((mx, my)):
            if click:
                print(12345)
                if meme==1 and uro ==1:
                    zadaniya(fiz2,2,1)
                if meme == 2 and uro ==1:
                    zadaniya(fiz3, 3,1)
                if meme ==1 and uro ==2:
                    zadaniya(inf2,2,2)

                if meme ==4 and uro ==2:
                    zadaniya(inf5,5,2)
        pygame.display.update()
def goodbie():
    sys.exit(0)
how_level=0
def beacoup_levels(bg,level,hero,how_level):
    left = right = False
    up = False
    entities.add(hero)
    x = y = 0
    for i in level:
        for j in i:
            if j == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if j == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "#":
                bd = lavadead(x, y)
                entities.add(bd)
                platforms.append(bd)
            if j == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while True:
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        if not pygame.sprite.collide_rect(hero, pr):
            screen.blit(bg, (0, 0))
            animatedEntities.update()
            camera.update(hero)
            hero.update(left, right, up, platforms)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
                if how_level ==11:
                    zadaniya(fiz1,1,1)
                if how_level ==22:
                    zadaniya(inf1,1,2)
        else:
            animatedEntities.empty()
            entities.empty()
            platforms.clear()
            if how_level ==1:
                return bonuslvl()
            if how_level ==2:
                return bonuslvl2()
            if how_level == 3:
                return level4()
            if how_level == 4:
                return level5()
        pygame.display.update()

def game():
    how_level=1
    bg = pygame.image.load('data/fon1.png')
    hero = Player(55, 555)
    level = load_level("level_1.txt")
    return beacoup_levels(bg, level, hero, how_level)
def bonuslvl():
    how_level=11
    bg = pygame.image.load('data/fon1.png')
    hero = Player(55, 355)
    level = load_level("level_1.txt")
    return beacoup_levels(bg, level, hero, how_level)
def bonuslvl2():
    how_level=22
    bg = pygame.image.load('data/fon2.png')
    hero = Player(55, 355)
    level = load_level("level_1.txt")
    return beacoup_levels(bg, level, hero, how_level)
def level2():
    how_level = 2
    bg = pygame.image.load('data/fon2.png')
    hero = Player(55,55)
    level = load_level("level_2.txt")
    return beacoup_levels(bg,level,hero,how_level)
def level3():
    how_level = 3
    bg = pygame.image.load('data/fon3.png')
    hero = Player(160,580)
    level= load_level("level_3.txt")
    return beacoup_levels(bg,level,hero,how_level)
def level4():
    how_level = 4
    bg = pygame.image.load('data/fon4.png')
    hero = Player(130,580)
    level = load_level("level_4.txt")
    return beacoup_levels(bg,level,hero,how_level)
def level5():
    how_level = 5
    bg = pygame.image.load('data/fon5.png')
    hero = Player(140, 500)
    level = load_level("level_5.txt")
    return beacoup_levels(bg,level,hero,how_level)
main_menu()