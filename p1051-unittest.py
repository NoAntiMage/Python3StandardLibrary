# Use assertIn() to test container membership.

import unittest


class SimplisticTest(unittest.TestCase):
    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
