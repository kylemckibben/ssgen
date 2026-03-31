import unittest

from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_on_base_class(self):
        n = HTMLNode()
        self.assertRaises(NotImplementedError)

    def test_props_to_html_with_props(self):
        n = HTMLNode(tag='<a>', value='link', props={'href':'localhost', 'target':'_blank'})
        expected = ' href="localhost" target="_blank"'
        self.assertEqual(n.props_to_html(), expected)

