import unittest

from src.textnode import TextNode
from src.enums.texttype import TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_text(self):
        node1 = TextNode("This is a text node", TextType.LINK, "fake.link")
        node2 = TextNode("This is a different text node", TextType.LINK, "fake.link")
        self.assertNotEqual(node1, node2)

    def test_not_eq_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_link(self):
        node1 = TextNode("This is a text node", TextType.LINK, "fake.link1")
        node2 = TextNode("This is a text node", TextType.LINK, "fake.link2")
        self.assertNotEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.LINK, "fake.link1")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()

