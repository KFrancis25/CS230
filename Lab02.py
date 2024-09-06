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
        return "48 mintues" #standard NBA game length

    def get_court_size(self):
        return "94 feet long, 50 feet wide" #NBA court size
    
class Tennis(Sport):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def get_equipment(self):
        return "Tennis"

    def team_size(self):
        return "2"

    def get_game_duration(self):
        return "30 to 60 minutes" 

    def get_court_size(self):
        return "78ft long by 36ft wide"


class TestBasketball(unittest.TestCase):

    def test_get_equipment(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_equipment(), "Basketball")

    def test_team_size(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.team_size, 5)

    def test_get_game_duration(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_game_duration(), "48 mintues")

    def test_get_court_size(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_court_size(), "94 feet long, 50 feet wide")

class TestTennis(unittest.TestCase):
     def test_get_equipment(self):
        game = Tennis("Tennis ", 2)
        self.assertEqual(game.get_equipment(), "Tennis")

     def test_team_size(self):
        game = Tennis("Tennis", 2)
        self.assertEqual(game.team_size, 2)

     def test_get_game_duration(self):
        game = Tennis("Tennis", 2)
        self.assertEqual(game.get_game_duration(), "30 to 60 minutes")

     def test_get_court_size(self):
        game = Tennis("Tennis", 2)
        self.assertEqual(game.get_court_size(), "78ft long by 36ft wide")
    
    
if __name__ == "__main__":
    unittest.main()
