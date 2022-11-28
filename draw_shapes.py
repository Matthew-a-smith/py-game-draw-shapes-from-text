# import pygame
# import class_shape
# import time (optional not needed)
# 
# pygame.init()
# while = true
# while shape = open('file.txt', "rt")
#   shape_line = shape
#   shape_list = []
# while shape line 
#   data = shape_line.split(":")
#   parms = data.split(",")
#   new_shape = data + parms 
#   shape_list.append
# while shape = repeat loop
# running = true
# while running
#   for shape in shape list
#   draw shapes from class, 'class_shape' use new_shape list get parms from data.split

import pygame
import class_shape
import time
pygame.init()

screen = pygame.display.set_mode([500, 500])

f_shape = open('shapes_draw.txt', "rt")
shape_line = f_shape.readline()
shape_list = []

while shape_line:
    line_data = shape_line.split(":")
    line_parms = line_data[1].split(",")
    print("shape" + str(line_parms[3]))
    new_shape = [line_data[0], line_parms]

    shape_list.append(new_shape)
    shape_line = f_shape.readline()

for shape in shape_list:
    print("shape =" + str(shape))
    
exit


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    for shape in shape_list:
        if shape [0] == "circle":
            class_shape.draw_circle(screen, shape[1][0], shape[1][1], shape[1][2], shape[1][3], shape[1][4], shape[1][5])

        if shape [0] == "rectangle":
            class_shape.draw_rectangle(screen, shape[1][0], shape[1][1], shape[1][2], shape[1][3], shape[1][4], shape[1][5], shape[1][6])

        if shape [0] == "triangle":
            class_shape.draw_triangle(screen, shape[1][0], shape[1][1], shape[1][2], shape[1][3], shape[1][4], shape[1][5], shape[1][6], shape[1][7], shape[1][8])
           
        if shape [0] == "line":
            class_shape.draw_line(screen, shape[1][0], shape[1][1], shape[1][2], shape[1][3], shape[1][4], shape[1][5], shape[1][6])

        time.sleep(1.2)
    
        pygame.display.flip()
pygame.quit()
    
        
        







    
        


                
            


        




    





