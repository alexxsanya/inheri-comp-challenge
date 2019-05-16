import unittest
from inheritance import Animal, Cow, Dog

class TestInheritanceClass(unittest.TestCase):
    
    def setUp(self):
        self.pow = Cow('red','male')
        self.james = Dog('james','brown')

    def test_cow_is_an_animal(self):
        self.assertIsInstance(self.pow,Animal)

    def test_cow_makes_mow_sound(self):
        self.assertEqual(self.pow.make_sound(),'Moooooow')
        self.assertNotEqual(self.pow.make_sound(),"Boooo")

    def test_check_cow_sex_is_male(self):
        self.assertEqual(self.pow.sex, 'male')
        self.assertNotEqual(self.pow.sex,"mafemalele")

    def test_dog_makes_boo_sound(self):
        self.assertEqual(self.james.make_sound(),'Boo boo')
        self.assertNotEqual(self.james.make_sound(),"Moooooow")

    def test_dog_name_is_james(self):
        self.assertEqual(self.james.name,'james')
        self.assertNotEqual(self.james.name,'steven')

if __name__ == '__main__':
    unittest.main()