"""
Build a class ScoreBoard with a private score.
Add a method to add points but ensure the score never becomes negative.
"""

class ScoreBoard:
    def __init__(self):
        self.__score = 0

    def add_points(self, points):
        if self.__score + points < 0:
            print("Score cannot become negative.")
        else:
            self.__score += points
            print(f"Score updated: {self.__score}")

    def get_score(self):
        return self.__score


score = ScoreBoard()
score.add_points(2)
score.get_score()
score.add_points(5)
score.get_score()