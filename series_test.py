import unittest

from series import format_series_name


class SeriesTest(unittest.TestCase):

    def test_format_series_name(self):
        given = 'New     Girl'
        expected = 'new-girl'
        self.assertEqual(expected, format_series_name(given))

        given = 'The Big Bang Theory'
        expected = 'the-big-bang-theory'
        self.assertEqual(expected, format_series_name(given))

        given = 'A     RaNDoM             Name'
        expected = 'a-random-name'
        self.assertEqual(expected, format_series_name(given))


if __name__ == '__main__':
    unittest.main()
