import os
import shutil

def populate_public_dir(path: str) -> None:
    """Clear contents of public/ and populate with contents of static/

    Arguments:
    path -- path to the public directory, passed in from main.py
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    static_path = os.path.abspath('./static/')
    copy_static_dir(static_path, path)

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
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, public_path)
        elif os.path.isdir(item_path):
            public_dir = os.path.join(public_path, item)
            os.mkdir(public_dir)
            copy_static_dir(item_path, public_dir)

    
