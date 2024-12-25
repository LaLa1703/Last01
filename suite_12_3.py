import unittest
from tests_12_3 import RunnerTest, TournamentTest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()