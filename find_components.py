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
    