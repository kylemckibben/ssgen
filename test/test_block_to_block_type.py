import unittest

from src.blocktype import BlockType
from src.helpers.block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_heading_one(self):
        block = "# Heading 1"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_block_heading_two(self):
        block = "## Heading 2"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_block_heading_three(self):
        block = "### Heading 3"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_block_heading_four(self):
        block = "#### Heading 4"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_block_heading_five(self):
        block = "##### Heading 5"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_block_heading_six(self):
        block = "###### Heading 6"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.HEADING)

    def test_invalid_heading(self):
        block = "#Not a Heading 1"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_block_code(self):
        block = "```\nThis is a code block\n```"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.CODE)

    def test_invalid_code(self):
        block = "```This is not a code block\n```"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_block_quote(self):
        block = "> this\n> is a\n> quote"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.QUOTE)

    def test_invalid_quote(self):
        block = "> this\n> is an\ninvalid\n> quote"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_block_unordered_list(self):
        block = "- this\n- is an\n- unordered\n- list"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        block = "- this\n- is an\n-invalid unordered\n- list"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_block_ordered_list(self):
        block = "1. this\n2. is an\n3. ordered\n4. list"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.ORDERED_LIST)

    def test_invalid_ordered_list(self):
        block = "1. this\n2. is an\n3.invalid ordered\n4. list"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)

    def test_block_paragraph(self):
        block = "This is a paragraph"
        res = block_to_block_type(block)
        self.assertEqual(res, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
