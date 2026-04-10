import os

from src.helpers.populate_public_dir import populate_public_dir

def main():
    path = os.path.abspath('./public/')
    populate_public_dir(path, './template.html')


if __name__ == "__main__":
    main()
