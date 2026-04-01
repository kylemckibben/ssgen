import unittest

from src.helpers import text_node_to_html_node
from src.textnode import TextNode
from src.texttype import TextType

class TestHelpers(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        expected = "This is a text node"
        self.assertEqual(html_node.value, expected)

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        expected = "<b>This is a bold node</b>"
        self.assertEqual(html_node.to_html(), expected)

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        expected = "<i>This is an italic node</i>"
        self.assertEqual(html_node.to_html(), expected)

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        expected = "<code>This is a code node</code>"
        self.assertEqual(html_node.to_html(), expected)

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "localhost")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        expected = '<a href="localhost">This is a link node</a>'
        self.assertEqual(html_node.to_html(), expected)

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "localhost/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        expected = '<img src="localhost/image.png" alt="This is an image node"></img>'
        self.assertEqual(html_node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
