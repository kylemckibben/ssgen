import re
from typing import List, Tuple

def extract_markdown_images(text: str) -> List[Tuple(str, str)]:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    images = re.findall(regex, text)
    return images
    
