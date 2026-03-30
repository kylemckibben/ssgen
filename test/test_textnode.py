import unittest

from src.textnode import TextNode
from src.texttype import TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        n1 = TextNode("This is a text node", TextType.BOLD)
        n2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(n1, n2)

    def test_not_eq_text(self):
        n1 = TextNode("This is a text node", TextType.LINK, "fake.link")
        n2 = TextNode("This is a different text node", TextType.LINK, "fake.link")
        self.assertNotEqual(n1, n2)

    def test_not_eq_type(self):
        n1 = TextNode("This is a text node", TextType.BOLD)
        n2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(n1, n2)

    def test_not_eq_link(self):
        n1 = TextNode("This is a text node", TextType.LINK, "fake.link1")
        n2 = TextNode("This is a text node", TextType.LINK, "fake.link2")
        self.assertNotEqual(n1, n2)

    def test_not_eq(self):
        n1 = TextNode("This is a text node", TextType.LINK, "fake.link1")
        n2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(n1, n2)


if __name__ == "__main__":
    unittest.main()

