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
        
if __name__ == "__main__":
    unittest.main()