class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
    
    def get_nationality(self):
        return self.nationality
    
    def get_goals(self):
        return self.goals
    
    def get_assists(self):
        return self.assists
    
    def assists_plus_goals(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} team {self.team} | goals {self.goals}, assists {self.assists}"
