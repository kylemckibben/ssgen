import unittest

from src.helpers.split_nodes_delimiter import split_nodes_delimiter
from src.nodes.textnode import TextNode
from src.enums.texttype import TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_two_bold(self):
        node = TextNode("This **is** **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_varied_delimiter(self):
        node = TextNode("This is **bold** and this is _italic_ and this is `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and this is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_opening_md(self):
        node = TextNode("**bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        expected = [TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_closing_md(self):
        node = TextNode("text _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        expected = [TextNode("text ", TextType.TEXT), TextNode("italic", TextType.ITALIC)]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_multiple_nodes(self):
        node1 = TextNode("text _italic_", TextType.TEXT)
        node2 = TextNode("**bold** text", TextType.TEXT)
        node3 = TextNode("This _is_ text", TextType.TEXT)
        node4 = TextNode("Plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3, node4], '_', TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            TextNode("Plain text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_with_not_text_type(self):
        node1 = TextNode("`code`", TextType.CODE)
        node2 = TextNode("**bold**text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        expected = [
            TextNode("`code`", TextType.CODE), 
            TextNode("bold", TextType.BOLD),
            TextNode("text", TextType.TEXT), 
        ]
        self.assertEqual(new_nodes, expected)

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
