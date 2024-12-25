import unittest
from runner import Runner
from runner_and_tournament1 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Runner1')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Runner2')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_chalenge(self):
        test_1 = Runner('Test 1')
        test_2 = Runner('Test 2')
        for _ in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)


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
