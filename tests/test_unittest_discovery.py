import unittest

from tests.run_tests import main


class ScaffoldTestRunner(unittest.TestCase):
    def test_function_tests_pass(self):
        self.assertEqual(main(), 0)
