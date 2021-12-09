import turtle as turtle_module
import random
turtle_module.colormode(255)
kev = turtle_module.Turtle()
kev.speed("fastest")
kev.penup()
kev.hideturtle()
color_list = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56), (35, 78, 89), (106, 139, 124), (152, 201, 229), (146, 125, 107)]
kev.setheading(225)
kev.forward(300)
kev.setheading(0)
number_of_dots = 160

for dot_count in range(1, number_of_dots + 1):
    kev.dot(20, random.choice(color_list))
    kev.forward(50)

    if dot_count % 10 == 0:
        kev.setheading(90)
        kev.forward(50)
        kev.setheading(180)
        kev.forward(500)
        kev.setheading(0)