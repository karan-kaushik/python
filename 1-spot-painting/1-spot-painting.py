# import colorgram

# image_colors = colorgram.extract("canvas.png", 10)

# colour_list = []
# for color in image_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colour_list.append((r, g, b))

# print(colour_list)
import random
import turtle as turtle_module
turtle_module.colormode(255)
colour_list = [(150, 143, 139), (124, 112, 110), (230, 240, 234), (122, 160, 205), (48, 101, 159), (140, 64, 88), (241, 232, 235), (243, 76, 34)]

slash = turtle_module.Turtle()
slash.speed("fastest")
slash.penup()
slash.hideturtle()
slash.setheading(225)
slash.forward(325)
slash.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    slash.dot(20, random.choice(colour_list))
    slash.forward(50)

    if dot_count % 10 == 0:
        slash.setheading(90)
        slash.forward(50)
        slash.setheading(180)
        slash.forward(500)
        slash.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
