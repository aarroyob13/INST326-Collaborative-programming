import unittest

from components import find_components

class TestFindComponents(unittest.TestCase):
    
    def setUp(self):
        """
        Set up a standard list of components before each test.
        """
        
        self.sample_components = [
            
            {"id" : "firewall", "requires" : [], "risk" : 2, "min_health": 50},
            {"id" : "mainframe", "requires" : ["firewall"], "risk" : 5, 
             "min_health": 40},
            {"id" : "camera_grid", "requires" : [], "risk" : 1, 
             "min_health": 20},
            {"id" : "vault_lock", "requires" : ["camera_grid"], "risk" : 2, 
             "min_health": 80},
            {"id" : "alarm", "requires" : [], "risk" : 2, "min_health": 50},
            
        ]
        
    def test_standard_filtering_and_sorting(self):
        """
        
        Returns unlocked items meeting the health requirement before being 
        sorted by risk than ID.
        
        """
        
        # 'firewall' is disabled; 'alarm' and 'camera_grid' has no 
        # requirements.
        # 'mainframe' is unlocked because 'firewall' is disabled.
        # 'vault_lock' is excluded because health (60) < min_health (80).
        
        result = find_components(self.sample_components, {"firewall"}, 60)
        result_ids = [comp["id"] for comp in result]
        
    def test_tie_breaker_sorting_by_id(self):
        """
        
        Components with equal risk are sorted alphabeticallly by ID.
        
        """
        
        comps = [
            
            {"id" : "zeta", "requires" : [], "risk" : 3, "min_health" : 10},
            {"id" : "alpha", "requires" : [], "risk" : 3, "min_health" : 10},
            {"id" : "beta", "requires" : [], "risk" : 3, "min_health" : 10}
        ]
        
        result = find_components(comps, set(), 100)
        self.assertEqual([c["id"] for c in result], ["alpha", "beta", "zeta"])
        
    def test_exact_min_health_boundary(self):
        """
        
        Component is avaliable when player health equals min_health.
        
        """
        
        comps = [
            
            {"id" : "sensor", "requires" : [], "risk" : 1, "min_health" : 50}
            
        ]
        
        result = find_components(comps, set(), 50)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "sensor")
        
    def test_multiple_dependencies_required(self):
        """
        
        Component unlocks only whenALL required IDs are disabled.
        
        """
        
        comps = [
            
            {"id" : "node_a", "requires" : [], "risk" : 1, "min_health" : 10},
            {"id" : "node_b", "requires" : [], "risk" : 1, "min_health" : 10},
            {"id" : "core", "requires" : ["node_a", "node_b"], "risk" : 4, 
             "min_health" : 10}
            
        ]
        
        # If only one required ID is disabled, 'core' remains locked.
        partial = find_components(comps, {"node_a"}, 100)
        self.assertEqual([c["id"] for c in partial], ["node_b"])
        
        # If both required ID is disabled, 'core' is unlocked.
        complete = find_components(comps, {"node_a", "node_b"}, 100)
        self.assertEqual([c["id"] for c in complete], ["core"])
        
    def test_empty_components_list(self):
        """
        
        Returns an empty list when given no components.
        
        """
        
        self.assertEqual(find_components([], set(), 100), [])
        
    def test_all_componets_disabled(self):
        """
        
        Returns an empty list when all components are already disabled.
        
        """
        
        all_ids = {c["id"] for c in self.sample_components}
        self.assertEqual(find_components(self.sample_components, all_ids,
                                         100), [])
        
    def test_raises_on_duplicate_component_id(self):
        """
        
        Raise a ValueError if two components share the same ID.
        
        """
        
        duplicate_comps = [
            
            {"id" : "firewall", "requires" : [], "risk" : 1, 
             "min_health" : 10},
            {"id" : "firewall", "requires" : [], "risk" : 2, 
             "min_health" : 20},
            
        ]
        
        with self.assertRaises(ValueError):
            find_components(duplicate_comps, set(), 100)
            
    def test_on_raise_or_invalid_id(self):
        """
        
        Raise a ValueError if a component ID is not a string or blank.
        
        """
        
        blank_id = [{"id" : " ", "requires" : [], "risk" : 1, 
                     "min_health" : 10}]
        none_id = [{"id" : None, "requires" : [], "risk" : 1, 
                     "min_health" : 10}]
        
        with self.assertRaises(ValueError):
            find_components(blank_id, set(), 100)
            
        with self.assertRaises(ValueError):
            find_components(none_id, set(), 100)
            
    def test_raises_on_nonexistent_dependency(self):
        """
        
        Raise a ValueError if 'requires' reference is an unknown component ID.
        
        """
        
        bad_dependency = [
            
            {"id" : "firewall", "requires" : ["ghost_node"], "risk" : 1, 
             "min_health" : 10}
            
        ]
        
        with self.assertRaises(ValueError):
            find_components(bad_dependency, set(), 100)
        
if __name__ == "__main__":
    unittest.main()