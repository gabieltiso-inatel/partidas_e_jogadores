class PlayersAndMatchesDatabase:
    def __init__(self, database):
        self.db = database

    def create_match(self, name, winner_name, score):
        query = "CREATE (:Match {name: $name, winner_name: $winner_name, score: $score})"
        parameters = {"name": name, "winner_name": winner_name, "score": score}
        self.db.execute_query(query, parameters)

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.name AS name, m.winner_name AS winner, m.score AS score"
        results = self.db.execute_query(query)
        return [f"{result['name']}: Winner -> {result['winner']}, Score -> {result['score']}" for result in results]

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_player_history(self, name):
        query = """
        MATCH (p:Player{name: $name})-[:PLAYED_IN]->(m:Match) 
        RETURN p.name AS player_name, m.name as match_name, m.score AS score, m.winner_name as winner
        """
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)

        matches = []
        for result in results:
            if result['player_name'] == result['winner']:
                matches.append(f"{result['match_name']} - {result['score']} - WIN")
            else:
                matches.append(f"{result['match_name']} - {result['score']} - LOSS")

        return matches


    def update_match(self, old_name, new_name):
        query = "MATCH (m:Match {name: $old_name}) SET m.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_player_match(self, player_name, match_name):
        query = "MATCH (a:Player {name: $player_name}) MATCH (b:Match {name: $match_name}) CREATE (a)-[:PLAYED_IN]->(b)"
        parameters = {"player_name": player_name, "match_name": match_name}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, name):
        query = "MATCH (m:Match {name: $name}) DETACH DELETE m"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
