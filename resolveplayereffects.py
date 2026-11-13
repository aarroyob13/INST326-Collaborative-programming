def resolve_player_effects(player_state, outcomes, rules):
    """Apply sequential rewards and penalties to a player state.

    Args:
        player_state (dict): Current 'health' (int), 'score' (int),
            and 'disabled_ids' (set[str]) for one player.
        outcomes (list[dict]): Ordered component-attempt outcomes
            with 'component_id' (str), 'status' (str), 'risk' (int).
        rules (dict): Numeric point and damage values by outcome.

    Returns:
        dict: Updated player state with bounded health, total
            score, and disabled component IDs.

    Raises:
        ValueError: If state or outcome records are inconsistent.
    """
    health = player_state.get("health")
    score = player_state.get("score")
    disabled_ids = set(player_state.get("disabled_ids", []))
    
    for outcome in outcomes:
        id_component = outcome.get("component_id")
        status = outcome.get("status")
        risk = outcome.get("risk")
        
        if status == "success":
            point = rules.get("success_points", 50)
            score += point * risk
            disabled_ids.add(id_component)
        