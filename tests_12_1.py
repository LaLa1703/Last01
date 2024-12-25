import unittest
from runner import Runner

class RunnersTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()


