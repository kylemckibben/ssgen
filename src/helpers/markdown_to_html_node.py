from typing import Dict, List, Tuple

from src.enums.blocktype import BlockType
from src.enums.texttype import TextType
from src.helpers.markdown_to_blocks import markdown_to_blocks
from src.helpers.block_to_block_type import block_to_block_type
from src.helpers.text_node_to_html_node import text_node_to_html_node
from src.helpers.text_to_textnodes import text_to_textnodes
from src.nodes.htmlnode import HTMLNode
from src.nodes.parentnode import ParentNode
from src.nodes.textnode import TextNode


def markdown_to_html_node(markdown: str) -> str:
    """Converts full markdown document into HTML by checking each block of
        the document. Handles nested structures (like lists) to add inner
        elements by first converting to Parent and Leaf nodes accordingly,
        followed by conversion to an HTMLNode.

    Arguments:
    markdown -- markdown document
    """
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tag = _get_tag(block_type, block)
        value = _get_value(block_type, block)
        # Code blocks get nested into a <pre> element
        if block_type == BlockType.CODE:
            html_nodes.append(ParentNode("pre", [
                ParentNode(tag, [
                    text_node_to_html_node(TextNode(value, TextType.TEXT))
                ])
            ]))
        # Quotes get '>' stripped from the front of each line
        elif block_type == BlockType.QUOTE:
            quote_body = []
            lines = block.split('\n')
            for line in lines:
                print(f'current line of quote: {line}')
                quote_body.append(line[1:])
            quote = ''.join(quote_body)
            quote = quote.strip()
            print(f'quote: {quote}')
            html_nodes.append(ParentNode(tag, _get_children(quote)))
        # Unordered lists get nested list elements with list syntax omitted
        elif block_type == BlockType.UNORDERED_LIST:
            list_nodes = []
            lines = block.split('\n')
            for line in lines:
                print(f'current line of unordered list: {line}')
                list_nodes.append(ParentNode("li", _get_children(line[2:])))
            print(f'unordered list items ({len(list_nodes)} items): {list_nodes.__repr__()}')
            html_nodes.append(ParentNode("ul", list_nodes))
        # Ordered lists get nested list elements with numbered syntax omitted
        elif block_type == BlockType.ORDERED_LIST:
            list_nodes = []
            list_count = 1
            lines = block.split('\n')
            for line in lines:
                print(f'current line of ordered list: {line}')
                line_num = f'{list_count}. '
                list_nodes.append(ParentNode("li", _get_children(line[len(line_num):])))
                list_count += 1
            print(f'ordered list items ({len(list_nodes)} items): {list_nodes.__repr__()}')
            html_nodes.append(ParentNode("ol", list_nodes))
        # Paragraphs need newlines converted to spaces
        elif block_type == BlockType.PARAGRAPH:
            remove_white_space = " ".join(value.split('\n'))
            html_nodes.append(ParentNode(tag, _get_children(remove_white_space)))
        # All other block types just use the original value returned
        else:
            html_nodes.append(ParentNode(tag, _get_children(value)))
    return ParentNode("div", html_nodes).to_html()

def _get_tag(block_type: str, block: str) -> str:
    """Determine parent tag of the given markdown block.

    Arguments:
    block_type -- block type of the markdown
    block -- block of markdown
    """
    match(block_type):
        case BlockType.PARAGRAPH:
            return 'p'
        case BlockType.HEADING: 
            level = _get_heading_level(block)
            return f'h{level}'
        case BlockType.CODE:
            return 'code'
        case BlockType.QUOTE:
            return 'blockquote'
        case BlockType.UNORDERED_LIST:
            return 'ul'
        case BlockType.ORDERED_LIST:
            return 'ol'

def _get_heading_level(block: str) -> int:
    """Count the number of octothorpes, '#', in the markdown tag to get the
        correct elemnt tag.

    Arguments:
    block -- block of markdown
    """
    octothorpe_count: int = 0
    idx: int = 0
    while block[idx] == '#':
        octothorpe_count += 1
        idx += 1
    return octothorpe_count
    
def _get_value(block_type: str, block: str) -> str:
    """Get the block body without the markdown tag.

    Arguments:
    block_type -- block type of the markdown
    block -- block of markdown
    """
    match(block_type):
        case BlockType.HEADING:
            level = _get_heading_level(block)
            start = level + 1
            return block[level + 1:]
        case BlockType.CODE:
            # '```\n' at the start is 4
            # '```' at the end is 3
            return block[4:-3]
        case _:
            return block

def _get_children(block: str) -> List[HTMLNode]:
    """Convert markdown block to a list of leaf nodes.

    block -- block of markdown
    """
    children = []
    text_nodes = text_to_textnodes(block)
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

