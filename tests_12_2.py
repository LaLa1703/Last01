import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Усейн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usain_nik(self):
        tournament = Tournament(distance=90, runners=[self.runner_usain, self.runner_nik])
        self.all_results = tournament.start()
        print(self.all_results)
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    def test_race_andrey_nik(self):
        tournament = Tournament(distance=90, runners=[self.runner_andrey, self.runner_nik])
        self.all_results = tournament.start()
        print(self.all_results)
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(distance=90, runners=[self.runner_usain, self.runner_andrey, self.runner_nik])
        self.all_results = tournament.start()
        print(self.all_results)
        self.assertTrue(self.all_results[max(self.all_results.keys())] == 'Ник')



if __name__ == '__main__':
    unittest.main()