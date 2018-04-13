import unittest


class BasicUnitTest2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("aaThis runs only once before all the test")

    def setUp(self):
        print("This runs every time before each the test")

    # test methods should start with 'test_'
    def test_method1(self):
        print("message from method 1")

    def test_method2(self):
        print("message from method 2")

    def tearDown(self):
        print("This runs every time after each the test")

    @classmethod
    def tearDownClass(cls):
        print("bbThis runs only once after all the test")



if __name__ == '__main__':
    unittest.main(verbosity=2)