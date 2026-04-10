import unittest

from src.helpers.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_valid_title(self):
        markdown = "# This is the Title\n\nand this is the document"
        title = extract_title(markdown)
        expected = "This is the Title"
        self.assertEqual(title, expected)

    def test_extract_missing_title(self):
        markdown = "This is missing any heading"
        with self.assertRaises(Exception):
            title = extract_title(markdown)

    def test_extract_wrong_heading(self):
        markdown = "## This is the wrong heading"
        with self.assertRaises(Exception):
            title = extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
