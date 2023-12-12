from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()  # will clear score prior its change
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.write_score()
