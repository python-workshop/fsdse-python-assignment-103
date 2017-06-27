from unittest import TestCase


class TestBuild(TestCase):
    def test_compress(self):
        try:
            from build import compress
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(compress(None), None)
        self.assertEqual(compress(''), '')
        # self.assertEqual(compress('AABBCC'), 'AABBCC')
        self.assertEqual(compress('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(compress('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(compress('AAABAACCDDDD'), 'A3BA2C2D4')
