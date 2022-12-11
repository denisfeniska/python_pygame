import pygame as pg
import time, random, sys
from pygame.locals import *


# define constants

fps = 25
# window_size
window_w = 600
window_h = 500
# one block-letter_size
block = 20
# cup_size
cup_h = 20
cup_w = 10
# time of moving with key press
side_freq = 0.15
down_freq = 0.1
# destination between window and cup
side_margin = int((window_w - cup_w * block) / 2)
top_margin = int(window_h - cup_h * block - 5)
# pattern_size
fig_w = 5
fig_h = 5
# figure's color
colors = tuple()
lightcolors = tuple()


# print(pg.font.get_fonts)


