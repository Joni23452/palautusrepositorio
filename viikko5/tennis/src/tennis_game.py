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
        player1_score = self.player1.get_player_score()
        player2_score = self.player2.get_player_score()
        game_score = game_score_to_text(player1_score, player2_score)
        return game_score
    
def scores_equal(score1, score2):
    return score1 == score2

def tied_at(score):
    if score == 0:
        return "Love-All"
    elif score == 1:
        return "Fifteen-All"
    elif score == 2:
        return "Thirty-All"
    else:
        return "Deuce"
    
def in_overtime(score1, score2):
    return score1 >= 4 or score2 >= 4

def overtime_score(score1, score2):
    score_difference = score1 - score2

    if score_difference == 1:
        return "Advantage player1"
    elif score_difference == -1:
        return "Advantage player2"
    elif score_difference >= 2:
        return "Win for player1"
    else:
        return "Win for player2"
    
def player_score_to_text(score):
    if score == 0:
        return "Love"
    elif score == 1:
        return "Fifteen"
    elif score == 2:
        return "Thirty"
    elif score == 3:
        return "Forty"
    
def game_score_to_text(score1, score2):
    if scores_equal(score1, score2):
        return tied_at(score1)
    elif in_overtime(score1, score2):
        return overtime_score(score1, score2)
    else:
        return player_score_to_text(score1) + "-" + player_score_to_text(score2)