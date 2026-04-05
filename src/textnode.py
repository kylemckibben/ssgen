from src.enums.texttype import TextType


class TextNode:
    """Class that represents inline text of HTML and Markdown
    
    Arguments:
    text (str) -- text content of the node
    text_type (TextType) -- type of test the node contains, member of TextType enum
    url (str | None) -- url of the node, if applicable (link or image)
    """
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url

    def __eq__(self, other: TextNode) -> bool:
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

