from typing import Dict, List


class HTMLNode:
    """Class that represents HTML tags

    Arguments:
    tag -- optional string representation of the HTML tag
    value -- optional string representation of the value inside the tags
    children -- options list of all tags that are children of the current tag
    props -- optional dictionary containing attributes in attribute:value format
    """
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: List[HTMLNode] | None = None, 
        props: Dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        """Will be implemented by child classes"""
        raise NotImplementedError

    def props_to_html(self):
        """Return text representation of props with a leading space for each key:value pair"""
        return ' ' + ' '.join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'

