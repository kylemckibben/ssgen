import unittest
from src.textnode import TextNode
from src.enums.texttype import TextType
from src.helpers.split_markdown import split_nodes_image, split_nodes_link


class TestSplitMarkdown(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
        )

    def test_split_images_no_image(self):
        node = TextNode("This is just text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [TextNode("This is just text", TextType.TEXT)],
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.duckduckgo.com) and a [second link](https://www.eff.org)",
            TextType.TEXT,
        ) 
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.duckduckgo.com"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.eff.org"),
            ],
        )
    def test_split_link_no_link(self):
        node = TextNode("This is just text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [TextNode("This is just text", TextType.TEXT)],
        )


if __name__ == "__main__":
    unittest.main()
