import unittest

from synthetic import add


class SyntheticTests(unittest.TestCase):
    def test_positive_negative_and_zero(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 3), -1)
        self.assertEqual(add(0, 0), 0)

    def test_invalid_boundary_inputs(self) -> None:
        for value in [True, 1.5, "1", None]:
            with self.subTest(value=value), self.assertRaises(TypeError):
                add(value, 1)
