import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'I\'m a test paragraph!')
        expected = '<p>I\'m a test paragraph!</p>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(tag=None, value='This is raw text')
        expected = 'This is raw text'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_no_value(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError):
            node_html = node.to_html() 

if __name__ == "__main__":
    unittest.main()
