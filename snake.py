from turtle import *

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# for i in range(len(snake) - 1)
# x = snake[i].xcor
# y = snake[i].ycor
# new = setposition(x-20, y-20)



UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = [Turtle("square") for _ in range(3)]
        self.create_snake()
        self.snakehead = self.snake[0]
        self.snakehead.color("green")
        self.snakehead.shape("circle")
        self.snakehead.shapesize(0.8, 1.1)



    def create_snake(self):
        for i in range(0, len(self.snake)):
            self.snake[i].color("yellow")
            self.snake[i].penup()
            self.snake[i].shapesize(0.9, 0.9)
            self.snake[i].setposition(START_POSITIONS[i])

    # def create_snake(self):
    #     for i in range(len(self.snake)):
    #         self.snake[i-1].color("white")
    #         self.snake[i-1].penup()
            # self.x = self.snake[i].xcor()
            # self.y = self.snake[i].ycor()
            # self.snake[i+1].setposition(self.x - 20, self.y - 20)


    def move(self):
        for j in range(len(self.snake) - 1, 0, -1):
            newpos = self.snake[j - 1].position()
            self.snake[j].setposition(newpos)
        self.snakehead.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.snakehead.heading() != DOWN:
            self.snakehead.setheading(UP)

    def turn_left(self):
        if self.snakehead.heading() != RIGHT:
            self.snakehead.setheading(LEFT)


    def turn_down(self):
        if self.snakehead.heading() != UP:
            self.snakehead.setheading(DOWN)

    def turn_right(self):
        if self.snakehead.heading() != LEFT:
            self.snakehead.setheading(RIGHT)


    def increase_snake(self):
        self.snake.append(Turtle("square"))
        self.snake[-1].color("yellow")
        self.snake[-1].penup()
        self.snake[-1].shapesize(0.9,0.9)
        self.move()

    def resetgame(self):
        for segment in self.snake:
            segment.goto(500, 500)
        self.snake = [Turtle("square") for _ in range(3)]
        self.create_snake()
        self.snakehead = self.snake[0]
        self.snakehead.color("green")
        self.snakehead.shape("circle")
        self.snakehead.shapesize(0.8, 1.1)
        self.move()




