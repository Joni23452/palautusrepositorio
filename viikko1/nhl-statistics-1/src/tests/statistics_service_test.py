import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_not_found_is_None(self):
        #self.assertAlmostEqual(self.stats.search("Semenko"), Player("Semenko", "EDM", 4, 12))
        self.assertIsNone(self.stats.search("Kalle"))

    def test_search_found_is_not_None(self):
        #self.assertAlmostEqual(self.stats.search("Semenko"), Player("Semenko", "EDM", 4, 12))
        #self.assertIsNone(self.stats.search("Kalle"))
        self.assertIsNot(self.stats.search("Semenko"), None)

    def test_team_without_players_is_empty_list(self):
        #self.assertAlmostEqual(self.stats.search("Semenko"), Player("Semenko", "EDM", 4, 12))
        #self.assertIsNone(self.stats.search("Kalle"))
        self.assertAlmostEqual(self.stats.team("TIIMI"), [])

    def test_top_one_returns_list(self):
        self.assertIs(type(self.stats.top(1)), type(list()))
        

    