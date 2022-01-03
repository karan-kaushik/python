from turtle import Turtle

SEGMENTS_STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for starting_position in SEGMENTS_STARTING_POSTIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(starting_position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range (len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.head.forward(MOVE_DISTANCE)
    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
