import os
import sys

from src.helpers.generate_page import generate_pages
from src.helpers.populate_public_dir import populate_public_dir

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    public_path = os.path.abspath('./docs/')
    content_path = os.path.abspath('./content/')
    template_path = './template.html'

    populate_public_dir(public_path)
    generate_pages(content_path, template_path, public_path, basepath)


if __name__ == "__main__":
    main()
