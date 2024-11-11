import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_response(self):
        return self.response

class PlayerStats:
    def __init__(self, reader):
        self.stats = reader.get_response()
        self.players = []
        for player_dict in self.stats:
            player = Player(player_dict)
            self.players.append(player)

    def get_stats(self):
        return self.stats
    
    def top_scorers_by_nationality(self, nationality):
        scorers_list = []
        for player in self.players:
            if player.get_nationality() == nationality:
                scorers_list.append((player, player.assists_plus_goals()))
        scorers_list.sort(key=lambda x: x[1], reverse=True) #https://stackoverflow.com/a/8459243

        return scorers_list

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for scorers_tuple in players:
            print(f"{scorers_tuple[0]}, total {scorers_tuple[1]} points")

if __name__ == "__main__":
    main()