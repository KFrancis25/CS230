# Authors: Kai Francis, Ryan Yonek
# Date: 8/28/24
# Unit Testing for Inheritance Class Method

# Unit tests
import unittest

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

    def team_size(self):
        return "5 people"

    def get_game_duration(self):
        return "40 mintues" #standard NBA game length

    def get_court_size(self):
        return "94 feet long, 50 feet wide" #NBA court size


class TestBasketball(unittest.TestCase):

    def test_get_equipment(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_equipment(), "Basketball")

    def test_team_size(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.team_size, 5)

    def test_get_game_duration(self):
        game = Basketball("Basketball", 5, "40 minutes")
        self.assertEqual(game.get_game_duration(), "40 minutes")

    def test_get_court_size(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_court_size(), "94 feet long, 50 feet wide")
    
    
if __name__ == "__main__":
    unittest.main()



        