
import pygame
class shape_draw:
    def __init__():
        print("nothing")
        

def draw_triangle(screen, red, blue, green, x1, y1, x2, y2, x3, y3):
    print("in shape_draw.polygon")
    pygame.draw.polygon(screen, (int(red), int(blue), int(green)), ((int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))))
    

def draw_rectangle(screen, red, blue, green, x1, y1, width, height):
    print("in shape_draw.rectangle")
    pygame.draw.rect(screen,(int(red), int(blue), int(green)), (int(x1), int(y1), int(width), int(height)))


def draw_circle(screen, red , blue, green, x1, y1, radius):
    print("in shape_draw.circle")
    pygame.draw.circle(screen, (int(red), int(blue), int(green)), (int(x1), int(y1)), (int(radius)))

def draw_line(screen, red, blue, green, x1, y1, x2, y2):
    print("in shape_draw.line")
    pygame.draw.line(screen, (int(red), int(blue), int(green)), (int(x1), int(y1)), (int(x2), int(y2)))