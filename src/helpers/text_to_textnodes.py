from typing import List

from src.nodes.textnode import TextNode
from src.enums.texttype import TextType
from src.helpers.split_markdown import split_nodes_image, split_nodes_link
from src.helpers.split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text: str) -> List[TextNode]:
    """Convert text to all appropriate textnode types

    Arguments:
    text -- text string to be converted
    """
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

