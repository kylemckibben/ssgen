import unittest

from src.helpers.extract_markdown_images import extract_markdown_images
from src.helpers.extract_markdown_links import extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images_single_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(matches, [("image", "https://i.imgur.com/zjjcJKZ.png")])

    def test_extract_markdown_images_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            matches, 
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/zjjcJKZ.png"),
            ]
        )

    def test_extract_markdown_images_only_links(self):
        matches = extract_markdown_images("This is a link [link](localhost)")
        self.assertListEqual(matches, [])

    def test_extract_links_single_link(self):
        matches = extract_markdown_links("This is a link [link](localhost)")
        self.assertListEqual(matches, [("link", "localhost")])

    def test_extract_links_multiple_links(self):
        matches = extract_markdown_links("This has [link1](localhost) and [link2](localhost:8080)")
        self.assertListEqual(
            matches,
            [
                ("link1", "localhost"),
                ("link2", "localhost:8080"),
            ]
        )

    def test_extract_links_only_images(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(matches, [])


if __name__ == "__main__":
    unittest.main()
