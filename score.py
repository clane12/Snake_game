from turtle import Turtle


ALIGN = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game = Turtle()
        self.game.hideturtle()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.sety(260)
        self.hideturtle()
        self.up_scoreboard()

    def up_scoreboard(self):
        self.clear()
        self.write(arg=f"   SCORE: {self.score}    HIGH SCORE: {self.highscore}", align=ALIGN, font=FONT)
    def incresesocre(self):
        self.score += 1
        self.up_scoreboard()

    def gameover(self):
        self.game.color("white")
        self.game.write(arg=f"GAME OVER", align='center', font=('Arial', 20, 'bold'))

    def highsc(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.up_scoreboard()
