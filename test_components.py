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
        
        
if __name__ == "__main__":
    unittest.main()