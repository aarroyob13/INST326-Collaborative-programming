def judge_player_attempts(attempts, round_seconds):
    """Judge each player's attempt independently of the other players
    
    Args:
        attempts (list[dict]): One record per player containing 'player_id' (str),
            'answer' (int or None), 'expected' (int), and 'elapsed seconds' (float).
        round_seconds (float): max allowed seconds per attempt.
        
    Return:
        dict[str, dict]: Results keyed by Player ID; each result includes 
        'status' (str) and 'timely' (bool). A late attempt only affects the
        corresponding player. 
        
    Raises: 
        ValueError: If times are negative or player IDs repeat
    
    """
    
    if round_seconds < 0:
        raise ValueError("round_seconds cannot be negative")
    results = {}
    seen_ids = []
    
    for attempt in attempts:
        player_id = attempt["player_id"]
        answer = attempt ["answer"]
        expected = attempt ["expected"]
        elapsed = attempt["elapsed_seconds"]
        
        # Validation: bad data stops the round
        if elapsed < 0:
            raise ValueError("elapsed_seconds cannot be negative")
        if player_id in seen_ids:
            raise ValueError("duplicate player ID: " + player_id)
        seen_ids.append(player_id)
        
        # Judge one player
        timely = elapsed <= round_seconds
        if not timely:
            status = "timed_out"
        elif answer is None:
            status = "no answer"
        elif answer == expected:
            status = "correct"
        else:
            status = "wrong"
        
        results[player_id] = {"status": status, "timely": timely}
        