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
