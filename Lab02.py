#Lab02
#Kai Francis
#Ryan Yonek

# Base class
class Sport:
    def __init__(self, name):
        self.name = name

    def get_equipment(self):
        return "Generic sports equipment"

# Derived class
class Basketball(Sport):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def get_equipment(self):
        return "Basketball"

# Unit tests
import unittest

class TestBasketball(unittest.TestCase):

    def test_get_equipment(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_equipment(), "Basketball")

    def test_team_size(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.team_size, 5)

# Author: Ryan Yonek
# Date: 9/2/24
# Adding two methods and unit tests to exisiting project
# 


# Import unit test
import unittest

# Base class
class Dog:
    def __init__(self, name):
        self.name = name

    def get_love(self):
        return "Is a good girl"
    
# Derived class
class Dori(Dog):
    def __init__(self, name, numSit):
        super().__init__(name)
        self.numSit = numSit

    def get_love(self):
        return "Is a good girl"

# Unit Tests
class TestDori(unittest.TestCase):

    def test_get_love(self):
        goodGirl = Dori("Is a good girl", 10)
        self.assertEqual(goodGirl.get_love(), "Is a good girl")

    def test_numSit(self):
        goodGirl = Dori("Is a good girl", 10)
        self.assertEqual(goodGirl.numSit, 10)

if __name__ == "__main__":
    unittest.main()
