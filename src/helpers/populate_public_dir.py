import os
import shutil

from src.helpers.generate_page import generate_page

def populate_public_dir(path: str, template: str) -> None:
    """Clear contents of public/ and populate with contents of static/

    Arguments:
    path -- path to the public directory, passed in from main.py
    template -- HTML template for content directory md files
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    static_path = os.path.abspath('./static/')
    content_path = os.path.abspath('./content/')
    copy_static_dir(static_path, path)
    copy_content_dir(content_path, path, template)

def copy_static_dir(path: str, public_path: str) -> None: 
    """Helper function to copy contents from static/ into public/ recursively

    Arguments:
    path -- current path in static directory
    public_path -- current path in public directory
    """
    ls = os.listdir(path)
    if len(ls) == 0:
        return
    for item in ls:
        print(f'Item being copied: {item}')
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print('is file')
            shutil.copy(item_path, public_path)
        elif os.path.isdir(item_path):
            public_dir = os.path.join(public_path, item)
            os.mkdir(public_dir)
            copy_static_dir(item_path, public_dir) 

def copy_content_dir(path: str, public_path: str, template: str) -> None:
    """Helper funciton to copy contents of content directory into public

    Arguments:
    path -- current path in content directory
    public_path -- current path in public directory
    template -- HTML template for md files
    """
    ls = os.listdir(path)
    if len(ls) == 0:
        return
    for item in ls:
        print(f'Item being copied: {item}')
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            generate_page(item_path, template, os.path.join(public_path, 'index.html'))
        elif os.path.isdir(item_path):
            public_dir = os.path.join(public_path, item)
            os.mkdir(public_dir)
            copy_content_dir(item_path, public_dir, template)

