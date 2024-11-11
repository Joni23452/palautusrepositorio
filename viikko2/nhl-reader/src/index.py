import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    #Tehtävä 10
    '''print("Oliot:")

    for player in players:
        if player.get_nationality() == 'FIN':
            print(player)'''

    # Tehtävä 11
    print("Pelaajat järjestyksessä")
    pelaajalista = []
    for player in players:
        if player.get_nationality() == 'FIN':
            pelaajalista.append((player, player.assists_plus_goals()))
    pelaajalista.sort(key=lambda x: x[1], reverse=True) #https://stackoverflow.com/a/8459243
    
    for pelaajatuple in pelaajalista:
        print(f"{pelaajatuple[0]}, total {pelaajatuple[1]} points")

if __name__ == "__main__":
    main()
