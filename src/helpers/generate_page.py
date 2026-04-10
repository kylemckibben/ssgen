import os

from src.helpers.extract_title import extract_title
from src.helpers.markdown_to_html_node import markdown_to_html_node

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    """Reads and converts a markdown file into HTML, inserting it into the HTML
        template given and writes to the specified destination.

    Arguments:
    from_path -- path to the markdown file
    template_path -- path to the HTML template
    dest_path -- path where generated page is written to
    """
    # print(f'Markdown file: {from_path}\nHTML template: {template_path}\nDestination: {dest_path}')
    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown)
    
    # print(f'Title = {title}')
    # print(f'Content = {content}')

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as file:
        file.write(template)

