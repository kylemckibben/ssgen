import re
from typing import List, Tuple

def extract_markdown_links(text: str) -> List[Tuple(str, str)]:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links = re.findall(regex, text)
    return links

