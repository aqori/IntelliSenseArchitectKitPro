# test_intellisensearchitectkitpro.py
"""
Tests for IntelliSenseArchitectKitPro module.
"""

import unittest
from intellisensearchitectkitpro import IntelliSenseArchitectKitPro

class TestIntelliSenseArchitectKitPro(unittest.TestCase):
    """Test cases for IntelliSenseArchitectKitPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IntelliSenseArchitectKitPro()
        self.assertIsInstance(instance, IntelliSenseArchitectKitPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IntelliSenseArchitectKitPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
