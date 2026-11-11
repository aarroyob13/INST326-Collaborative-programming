def find_components(components, disable_id, health):
    """
    Find components and player's health status based on the given input.
    
    Args:
    
        components (list[dict]): Components record with string 'id', list[str] 
        'requires', int 'risk', and int 'min_health'
    
        disable_id (set[str]): Determine if the ID is disabled or not.
    
        health(int): The players current health.
        
    Returns:
    
        list[dict]: Avaliable components ordered by risk first, then by 
        Component Id.  Exclude disabled items.
        
    Raise:
    
        ValueError: If component IDs or dependencies are invalid.
    
    """
    
    # Validate the component IDs (Make sure that the component ID has non-empty
    # strings and no duplicates)
    
    valid_ids = set()
    
    for comp in components:
        
        comp_id = comp.get("id")
        if not isinstance(comp_id, str) or not comp_id.strip():
            raise ValueError("Component ID must be a non-empty string.")
        
        if comp_id in valid_ids:
            raise ValueError(f"Duplicate component ID found: '{comp_id}'")
        
        valid_ids.add(comp_id)
    
    #    