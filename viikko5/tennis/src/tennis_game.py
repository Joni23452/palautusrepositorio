class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

    def get_name(self):
        return self.name
    
    def get_player_score(self):
        return self.score

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player1.add_point()
        elif player_name == self.player2.get_name():
            self.player2.add_point()

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1.get_player_score() == self.player2.get_player_score():
            if self.player1.get_player_score() == 0:
                score = "Love-All"
            elif self.player1.get_player_score() == 1:
                score = "Fifteen-All"
            elif self.player1.get_player_score() == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.player1.get_player_score() >= 4 or self.player2.get_player_score() >= 4:
            minus_result = self.player1.get_player_score() - self.player2.get_player_score()

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.get_player_score()
                else:
                    score = score + "-"
                    temp_score = self.player2.get_player_score()

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
