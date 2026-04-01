import unittest

from src.helpers.split_nodes_delimiter import split_nodes_delimiter
from src.textnode import TextNode
from src.texttype import TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode(" word", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_opening_md(self):
        node = TextNode("**bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        expected = [TextNode(" text", TextType.TEXT), TextNode("bold", TextType.BOLD)]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_closing_md(self):
        node = TextNode("text __italic__", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '__', TextType.ITALIC)
        expected = [TextNode("text ", TextType.TEXT), TextNode("italic", TextType.ITALIC)]

    def test_split_nodes_delimiter_with_multiple_nodes(self):
        node1 = TextNode("text __italic__", TextType.TEXT)
        node2 = TextNode("**bold** text", TextType.TEXT)
        node3 = TextNode("This __is__ text", TextType.TEXT)
        node4 = TextNode("Plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3, node4], '__', TextType.ITALIC)
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("**bold** text", TextType.TEXT),
            TextNode("This ", TextType.TEXT),
            TextNode(" text", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode("Plain text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_not_text_type(self):
        node1 = TextNode("`code`", TextType.CODE)
        node2 = TextNode("**bold**text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        expected = [
            TextNode("`code`", TextType.CODE), 
            TextNode("text", TextType.TEXT), 
            TextNode("bold", TextType.BOLD),
        ]

    def test_split_nodes_delimiter_with_wrong_delimiter_type(self):
        node = TextNode("`code`", TextType.TEXT)
        with self.assertRaises(ValueError) as ve:
            new_nodes = split_nodes_delimiter([node], "`", TextType.BOLD)

    def test_split_nodes_delimiter_with_unmatching_delimiter(self):
        node = TextNode("This is a text with a `code block** word", TextType.TEXT)
        with self.assertRaises(Exception) as e:
            split_nodes_delimiter([node], '`', TextType.CODE)


if __name__ == "__main__":
    unittest.main()
