def calculate_standings(players, completion_targets):
    """Rank players using completion, points, and tie-break rules.

    Args:
        players (list[dict]): Player records with 'name' (str),
            'score' (int), 'health' (int), 'disabled_ids' (set[str]),
            and 'total_time' (float).
        completion_targets (dict[str, int]): Required number of
            components for each player, keyed by player name.

    Returns:
        list[dict]: Ranked records with 'rank' (int), 'name'
            (str), and 'completed' (bool). Equal results share
            ranks; completion, score, health, and time are compared.

    Raises:
        ValueError: If names repeat or required fields are absent.
    """
    required_fields = ["name", "score", "health", "disabled_ids", "total_time"]
    checked_names = set()
    records = []

    #Checks the input to see if any field is misisng/repeating
    for player in players:
        for field in required_fields:
            if field not in player:
                raise ValueError(field + "is missing from Player record")


        name = player["name"]
        if name in checked_names:
            raise ValueError(name + " is duplicated in the player list")
        checked_names.add(name)


        if name not in completion_targets:
            raise ValueError(name + "is not in completion target")

        #Sorts the the players by the completion, score, and health, and time
        completed = len(player["disabled_ids"]) >= completion_targets[name]


        key = (-int(completed), -player["score"], -player["health"],
               player["total_time"])
        records.append((key, name, completed))

    records.sort()

    #Assign the  ranks
    standings = []
    previous_key = None
    rank = 0

    for position in range(len(records)):
        key, name, completed = records[position]
        if key != previous_key:
            rank = position + 1
            previous_key = key
        standings.append({"rank": rank, "name": name, "completed": completed})

    return standings