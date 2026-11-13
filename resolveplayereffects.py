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
    disabled_ids = player_state.get("disabled_ids")

    # Checks if state records are inconsistent
    if health is None or score is None or disabled_ids is None:
        raise ValueError("State records are incosistent.")

    update_disabled_ids = set(disabled_ids)  # Create a copy to avoid mutating the original set
    
    # Iterate through each outcome and apply effects
    for outcome in outcomes:
        id_component = outcome.get("component_id")
        status = outcome.get("status")
        risk = outcome.get("risk")

        # Checks if outcome records are inconsistent
        if id_component is None or status is None or risk is None:
            raise ValueError("Outcome records are inconsistent.")

        # Apply effects based on outcome status
        if status == "success":
            point = rules.get("success_points", 50)
            score += point * risk
            update_disabled_ids.add(id_component)
        else:
            damage = rules.get("failure_damage", 20)
            health -= damage * risk

    # Clamp health to [0, 100] range
    if health < 0:
        health = 0
    elif health > 100:
        health = 100

    # Return the updated player state
    return {
        "health": health,
        "score": score,
        "disabled_ids": update_disabled_ids
    }
