from src.textnode import TextNode
from src.texttype import TextType
from src.helpers.extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    """Split image markdown from text and convert to list of correct node types

    Arguments:
    old_nodes -- list of text nodes to be parsed into image and text types
    """
    new_nodes = []
    for node in old_nodes:
        split_nodes = []
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            for image in images:
                before, after = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                if before != "":
                    split_nodes.append(TextNode(before, TextType.TEXT))
                split_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                remaining_text = after
            if remaining_text != "":
                split_nodes.append(TextNode(remaining_text, TextType.TEXT))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    """Split link markdown from text and convert to list of correct node types
    
    Arguments:
    old_nodes -- list of text nodes to be pares into link and text types
    """
    new_nodes = []
    for node in old_nodes:
        split_nodes = []
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            for link in links:
                before, after = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                if before != "":
                    split_nodes.append(TextNode(before, TextType.TEXT))
                split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                remaining_text = after
            if remaining_text != "":
                split_nodes.append(TextNode(remaining_text, TextType.TEXT))
            new_nodes.extend(split_nodes)
    return new_nodes

