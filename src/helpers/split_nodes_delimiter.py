import re
from typing import List
from src.textnode import TextNode
from src.texttype import TextType

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    """Split a list of text node of type TEXT into a list of text nodes of type TEXT and the specified type
        passed in as an argument. The type passed in should match the delimiter or the function will return
        a list identical to the list of old nodes.

    Arguments:
    old_nodes -- list of text nodes to be parsed based on the delimiter and type
    delimiter -- symbol to check for which corresponds to mark down ('**' for bold, '__' for italics, '`' for code)
    text_type -- the text_type that corresponds to the delimiter passed in
    """
    _verify_delimiter_and_type_match(delimiter, text_type)
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif not node.text.__contains__(delimiter):
            new_nodes.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise Exception('Error: closing delimiter not found')
        else:
            search_delim = re.search(re.escape(delimiter) + '.*' + re.escape(delimiter), node.text)
            open_delim_idx, close_delim_idx = search_delim.span(0)
            split_nodes = []
            if open_delim_idx > 0:
                split_nodes.append(TextNode(node.text[:open_delim_idx], TextType.TEXT))
            if close_delim_idx < len(node.text):
                split_nodes.append(TextNode(node.text[close_delim_idx:], TextType.TEXT))
            split_nodes.append(
                    TextNode(node.text[open_delim_idx+len(delimiter):close_delim_idx-len(delimiter)], 
                    text_type)
            )
            new_nodes.extend(split_nodes)
    return new_nodes

def _verify_delimiter_and_type_match(delimiter: str, text_type: TextType) -> None:
    """Verifies that the delimiter and type match correctly

    Arguments:
    delimiter -- the delimiter given to split_nodes_delimiter
    text_type -- the text_type given to split_nodes_delimiter 
    """
    if (
        (delimiter == "**" and text_type != TextType.BOLD) or
        (delimiter == "__" and text_type != TextType.ITALIC) or
        (delimiter == "`" and text_type != TextType.CODE)
    ):
        raise ValueError(f'Delimiter {delimiter} does not match text type {text_type}')

