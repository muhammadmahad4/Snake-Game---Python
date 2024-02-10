from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_nums in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_nums - 1].xcor()
                new_y = self.segments[seg_nums - 1].ycor()
                self.segments[seg_nums].goto(new_x, new_y)

        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segs in self.segments:
            segs.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
