from typing import Dict
from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """Class that handles the nesting of HTML nodes

    Arguments:
    tag -- string representation of the parent HTML tag
    children -- list of nested HTML tags
    props -- optional dictionary containing attributes in attribute:value format for the parent tag
    """
    def __init__(
        self, 
        tag: str, 
        children: List[HTMLNode], 
        props: Dict[str, str] = None
    ) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError('Parent nodes must have a tag')
        if self.children is None:
            raise ValueError('Parent must have children')
        props_str = self.props_to_html() if self.props else ''
        children_str = "".join([child.to_html() for child in self.children])
        return f'<{self.tag}{props_str}>{children_str}</{self.tag}>'

