import unittest


class SyntheticCanaryTests(unittest.TestCase):
    def test_synthetic_canary(self) -> None:
        self.assertEqual(2 + 2, 4)


if __name__ == "__main__":
    unittest.main()
