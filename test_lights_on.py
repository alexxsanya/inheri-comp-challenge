import unittest 
from lights_on import evening_time

class TestLightsOnsystem(unittest.TestCase):

    def test_evening_time(self):
        time = 19
        self.assertEqual(evening_time(time),True)
        self.assertNotEqual(evening_time(6), True)

if __name__ == "__main__":
    unittest.main()
