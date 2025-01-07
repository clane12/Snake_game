from turtle import *
import random

# MEAT = Turtle("circle")
# MEAT.color("blue")
# MEAT.penup()
#
# class Food:
#
#     def __init__(self):
#         self.location = MEAT.position()
#
#     def random_meatpos(self):
#         x = random.randint(-400, 400)
#         y = random.randint(-300, 300)
#         MEAT.setposition(x, y)
#

class Food(Turtle): # here i inherited the functionalities of class Turtle and therefore made our food class
                    # to be able to do everything that turtle class can.
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.randon_location() # did this so when the class is called this function will be automatically
                                # run without calling it personally.

    def randon_location(self):
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        self.setposition(x, y)

