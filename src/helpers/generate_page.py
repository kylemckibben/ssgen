import os

from src.helpers.extract_title import extract_title
from src.helpers.markdown_to_html_node import markdown_to_html_node

def generate_pages(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    """Recursive function to generate pages from all markdown inside of contents directory

    Arguments:
    from_path -- path to the markdown file
    template_path -- path to the HTML template
    dest_path -- path where generated page is written to
    basepath -- root path of the site
    """
    ls = os.listdir(from_path)
    if len(ls) == 0:
        return
    for item in ls:
        item_path = os.path.join(from_path, item)
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, os.path.join(dest_path, 'index.html'), basepath)
        elif os.path.isdir(item_path):
            public_dir = os.path.join(dest_path, item)
            os.mkdir(public_dir)
            generate_pages(item_path, template_path, public_dir, basepath)

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    """Reads and converts a markdown file into HTML, inserting it into the HTML
        template given and writes to the specified destination.

    Arguments:
    from_path -- path to the markdown file
    template_path -- path to the HTML template
    dest_path -- path where generated page is written to
    basepath -- root path of the site
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
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as file:
        file.write(template)

