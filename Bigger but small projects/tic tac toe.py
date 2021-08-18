import pygame as pg
import sys
import numpy

pg.init()

screen_width = 600
screen_height = 600
color_bg = (28,170,156)
line_color = (13, 104, 112)
ROWS = 3
COLUMS = 3

screen = pg.display.set_mode( (screen_width,screen_height) )
pg.display.set_caption("Dumb TIC TAC TOE")
screen.fill(color_bg)

board = numpy.zeros((ROWS,COLUMS))
#print(board)

def draw_lines():
    pg.draw.line(screen, line_color, (0,200), (600,200), 15)
    pg.draw.line(screen, line_color, (0, 400), (600, 400), 15)
    pg.draw.line(screen, line_color, (200, 0), (200, 600), 15)
    pg.draw.line(screen, line_color, (400, 0), (400, 600), 15)

def mark_circle(row , colum, player):
    board[row][colum] == player

def mark_square(row, colum, player):
    pass

def khali_hai_ki_ni(row, colum):
    if board[row][colum] == 0:
        return True
    else:
        return False

draw_lines()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()