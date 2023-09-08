import unittest

import lesson2

release_name = 'lesson'

class CalTest(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.cal = lesson2.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    # @unittest.skip('skip!') # スキップ
    @unittest.skipIf(release_name=='lesson', 'skip!!') # 条件付きスキップ
    def test_add_num_and_double(self):
        cal = lesson2.Cal()
        self.assertEquals(
            cal.add_num_and_double(1, 1), 4
        )
        """
        assertEqual(a, b)   a == b
        assertNotEqual(a, b)    a != b
        assertTrue(x)   bool(x) is True
        assertFalse(x)  bool(x) is False
        assertIs(a, b)  a is b
        assertIsNot(a, b)   a is not b
        assertIsNone(x) x is None
        assertIsNotNone(x)  x is not None
        assertIn(a, b)  a in b
        assertNotIn(a, b)   a not in b
        assertIsInstance(a, b)  isinstance(a, b)
        assertNotIsInstance(a, b)   not isinstance(a, b)
        """

    def test_add_num_and_double_raise(self):
        cal = lesson2.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')

if __name__ == '__main__':
    unittest.main()