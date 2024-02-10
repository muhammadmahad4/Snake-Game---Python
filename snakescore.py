from turtle import Turtle
data1 = open('data.txt')
score = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = score
        self.high_score = int(data1.read())
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f'scoreboard: {self.score} High Score: {self.high_score}', move=False, align='center', font=('Courier', 15, 'normal'))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(f"{self.high_score}")


        self.score = 0
        self.clear()
        self.update_scoreboard()
    def score_up(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
