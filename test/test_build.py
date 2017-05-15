from unittest import TestCase


class TestBuild(TestCase):
# check wheter string is empty or not
#check if value is string only
#check the output of the value

    def test_check_whether_string_is_empty_or_not(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failed")

        result = build(None)
        self.assertEqual(None,result)

    def test_check_if_value_is_string_only(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failed")

        result = build("")
        self.assertEqual("", result)


    def test_check_the_output_of_the_value(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failed")

        result = build("selllf")
        self.assertEqual("sel3f", result)


