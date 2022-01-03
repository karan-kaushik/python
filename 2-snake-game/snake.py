from turtle import Turtle

SEGMENTS_STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

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
        self.segments[0].forward(MOVE_DISTANCE)
