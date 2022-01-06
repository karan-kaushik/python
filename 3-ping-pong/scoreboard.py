from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write("{}".format(self.l_score), align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write("{}".format(self.r_score), align=ALIGNMENT, font=FONT)
        
    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write("GAME OVER!\nLeft wins!", align=ALIGNMENT, font=FONT)
        elif self.r_score > self.l_score:
            self.write("GAME OVER!\nRight wins!", align=ALIGNMENT, font=FONT)
