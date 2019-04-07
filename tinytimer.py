import pygame
from pygame.locals import *

COLOR_BACKGROUND = [128, 0, 128]
COLOR_WHITE = (255, 255, 255)
FPS = 60
H_SIZE = 600  
W_SIZE = 800
MX_TIME = 300

pygame.init()


surface = pygame.display.set_mode((W_SIZE, H_SIZE))

clock = pygame.time.Clock()
timer = [0.0]
dt = 1.0 / FPS
timer_font = pygame.font.SysFont("Calibri", 100)

while True:
    clock.tick_busy_loop(60)
    surface.fill(COLOR_BACKGROUND)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    timer[0] += dt
    MX_TIME -= dt
    time = int(MX_TIME)   
    time_string = str(time)

    time_blit = timer_font.render(time_string, 1, COLOR_WHITE)
    time_blit_size = time_blit.get_size()
    surface.blit(time_blit,(W_SIZE / 2 - time_blit_size[0] / 2, H_SIZE / 2 - time_blit_size[1] / 2))

    pygame.display.flip()
