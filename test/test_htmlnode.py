import unittest

from src.nodes.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_on_base_class(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_with_props(self):
        node = HTMLNode(tag='<a>', value='link', props={'href':'localhost', 'target':'_blank'})
        expected = ' href="localhost" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()
