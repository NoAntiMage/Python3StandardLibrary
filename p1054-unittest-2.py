import unittest


class EqualityTest(unittest.TestCase):
    def testExpectEqual(self):
        self.assertEqual(1, 3 - 2)

    def testExpectEqualFails(self):
        self.assertNotEqual(2, 3 - 2)

    def testExpectNotEqual(self):
        self.assertNotEqual(2, 3 - 2)

    def testExpectNotequalFails(self):
        self.assertNotEqual(1, 3 - 2)

