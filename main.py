from database import Database
from matches_and_players_database import PlayersAndMatchesDatabase

db = Database("<YOUR_BOLT_URL>", "<YOUR_BOLT_USERNAME>", "<YOUR_BOLT_PASSWORD>")
db.drop_all()

players_and_matches_db = PlayersAndMatchesDatabase(db)

players = [
    "Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams",
    "Maria Sharapova", "Andy Murray", "Simona Halep", "Stefanos Tsitsipas"
]

for player in players:
    players_and_matches_db.create_player(player)

matches = [
    {"name": "Wimbledon 2023 Final", "winner_name": "Roger Federer", "score": "6-4, 7-6, 6-3"},
    {"name": "French Open 2023 Final", "winner_name": "Rafael Nadal", "score": "7-5, 6-3, 6-1"},
    {"name": "US Open 2023 Final", "winner_name": "Novak Djokovic", "score": "6-4, 7-6, 6-2"},
    {"name": "Australian Open 2023 Final", "winner_name": "Serena Williams", "score": "6-3, 6-4"},
]

for m in matches:
    players_and_matches_db.create_match(
            name=m["name"],
            winner_name=m["winner_name"],
            score=m["score"]
    )

players_and_matches_db.insert_player_match("Roger Federer", "Wimbledon 2023 Final")
players_and_matches_db.insert_player_match("Maria Sharapova", "Wimbledon 2023 Final")
players_and_matches_db.insert_player_match("Rafael Nadal", "French Open 2023 Final")
players_and_matches_db.insert_player_match("Stefanos Tsitsipas", "French Open 2023 Final")
players_and_matches_db.insert_player_match("Novak Djokovic", "US Open 2023 Final")
players_and_matches_db.insert_player_match("Andy Murray", "US Open 2023 Final")
players_and_matches_db.insert_player_match("Serena Williams", "Australian Open 2023 Final")
players_and_matches_db.insert_player_match("Simona Halep", "Australian Open 2023 Final")

# Print the list of players and matches
print("Players:")
for player in players_and_matches_db.get_players():
    print(player)

print("\nMatches:")
for match in players_and_matches_db.get_matches():
    print(match)

player_name = "Roger Federer"

print(f"\nMatch history for {player_name}:")
match_history = players_and_matches_db.get_player_history(player_name)
for match_result in match_history:
    print(match_result)

# players_and_matches_db.update_match("Wimbledon 2023 Final", "Updated Wimbledon 2023 Final")
# players_and_matches_db.delete_match("Wimbledon 2023 Final")

# players_and_matches_db.update_player("Roger Federer", "Updated Roger Federer")
# players_and_matches_db.delete_player("Roger Federer")
