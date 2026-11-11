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
    
    # Check and validate all listed dependencies against existing component 
    # IDs.
    
    for comp in components:
        for req_id in comp.get("requires", []):
            if req_id not in valid_ids:
                raise ValueError(
                    f"Component '{comp['id']}' has an invalid dependency: \
                    '{req_id}'"
                )
                
    # Filter for elgible components:
    avaliable = []
    
    for comp in components:
        comp_id = comp["id"]
        
    # Skip if already disabled
    if comp_id in disabled_dis:
        continue
    
    # Skip if player's current health is below the minimum requirement.
    if health < comp["min_health"]:
        continue
    
    # Check if all prerequisite components are in disabled_ids
    all_reqs_met = True
    for req_id in comp["requires"]:
        if req_id not in disable_ids:
            all_reqs_met = False
            break
        
    if all_reqs_met:
        avaliable.append(comp)