
# How to run two or more testcase classes

import unittest
from UnitTest.test_suite.BasicUnitTest1 import BasicUnitTest1
from UnitTest.test_suite.BasicUnitTest2 import BasicUnitTest2

# Get the test cases from class 1 and 2
test1 = unittest.TestLoader().loadTestsFromTestCase(BasicUnitTest1)
test2 = unittest.TestLoader().loadTestsFromTestCase(BasicUnitTest2)

# create a suite containing all the tests
test = unittest.TestSuite([test1, test2])

# Run the test
unittest.TextTestRunner(verbosity=2).run(test)
