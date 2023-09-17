import turtle

ALIGN = "center"
font = ("ArcadeClassic", 24, "normal")
with open("highest_score.txt", "r+") as f:
    sc = f.read()

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.highscore_for_game = int(sc)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
        self.goto(150, 270)
        self.write(f"High Score:{self.highscore_for_game}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER", align="center", font=("Chiller", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def update_high_score(self):
        with open("highest_score.txt", 'r+') as f:
            high_score = int(f.read())
            if self.score > high_score:
                f.write(str(self.score))
                self.highscore_for_game=self.score
