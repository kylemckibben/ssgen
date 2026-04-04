from typing import List

def markdown_to_blocks(markdown: str) -> List[str]:
    """Take markdown string and convert it to blocks. blocks are indicated by
        a separation of a blank line.

    Arguments:
    markdown -- markdown file text
    """
    blocks = markdown.split('\n\n')
    for i in range(len(blocks)):
        block = blocks[i]
        block = block.strip()
        if block == "":
            del blocks[i]
        else:
            blocks[i] = block
    return blocks
    
