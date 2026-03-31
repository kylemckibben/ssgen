from src.textnode import TextNode
from src.texttype import TextType


def main():
    text_node = TextNode(
            "This is some anchor text",
            TextType.BOLD,
        )

    print(text_node)


if __name__ == "__main__":
    main()
