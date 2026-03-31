from typing import Dict
from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """Class that represents a single HTML tag with no children

    Arguments:
    tag -- string representation of the HTML tag, required but can be None
    value -- string representation of the value inside the tags
    props -- optional dictionary containing attributes in attribute:value format
    """
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: Dict[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError('Leaf nodes must have a value')
        if self.tag is None:
            return self.value
        props_html = self.props_to_html() if self.props else '' 
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode(tag={self.tag}, value={self.value}, props={props_str})' 

