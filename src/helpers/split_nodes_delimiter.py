from typing import List
from src.textnode import TextNode
from src.enums.texttype import TextType

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
        if node.text_type != TextType.TEXT or not node.text.__contains__(delimiter):
            new_nodes.append(node)
        else:
            split_nodes = []
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception('Error: closing delimiter not found')
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
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

