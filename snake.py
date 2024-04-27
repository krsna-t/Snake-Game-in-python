from turtle import *

move_dist=20
starting_postions=[(0,0),(-20,0),(-40,0)]

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()

    def create_snake(self):
        for position in starting_postions:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())    

    def move(self):
        for seg_num in range(len(self.segment) -1,0,-1):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y) 
        self.segment[0].forward(move_dist)


    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
         if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
         if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)


    def right(self):
         if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)


  # time.sleep(0.99)
    # for seg in segment:
    #     seg.forward(20)
    #screen.ontimer(move, 100) move ek function hai jo hum log ko khud se define karne padega  
    # time.sleep(0.1)                     