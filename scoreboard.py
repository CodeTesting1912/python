from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 15, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-200, 270)
        self.score = 0
        self.high_score = self.show_high_score()
        self.score_text()
        self.write_high_score()


    def score_text(self):
        self.write(f"Score : {self.score}", True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", True, align=ALIGN, font=FONT)
        self.save_highest_score()

    def new_score(self):
        self.clear()
        self.score += 1
        self.goto(-200, 270)
        self.score_text()
        self.high_score = self.show_high_score()
        self.write_high_score()
    
    def save_highest_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open(r"high_score.txt", mode="w") as file:
                file.write(str(self.high_score))


    def show_high_score(self):            
        with open(r"high_score.txt", mode="r") as file:
           return int(file.read())
        
    
    def write_high_score(self):
        self.goto(50, 270)
        self.write(f"High Score : {self.high_score}", True, align=ALIGN, font=FONT)
        
