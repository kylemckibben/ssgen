from src.blocktype import BlockType

def block_to_block_type(block: str) -> BlockType:
    """Returns the block type of the given markdown block

    Arguments:
    block -- block of markdown text
    """
    if _is_heading(block):
        return BlockType.HEADING
    if _is_code(block):
        return BlockType.CODE
    if _is_quote(block):
        return BlockType.QUOTE
    if _is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if _is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

# Helper functions to clean up the condition logic in the main function
def _is_heading(block:str) -> bool:
    if (
        block[:2] == "# " or
        block[:3] == "## " or
        block[:4] == "### " or
        block[:5] == "#### " or
        block[:6] == "##### " or
        block[:7] == "###### "
    ):
        return True
    return False

def _is_code(block: str) -> bool:
    if block[:4] == "```\n" and block[-3:] == "```":
        return True
    return False

def _is_quote(block: str) -> bool:
    lines = block.split('\n')
    for line in lines:
        if line[0] != '>':
            return False
    return True

def _is_unordered_list(block: str) -> bool:
    lines = block.split('\n')
    for line in lines:
        if line[:2] != "- ":
            return False
    return True

def _is_ordered_list(block: str) -> bool:
    lines = block.split('\n')
    line_num = 1
    for line in lines:
        if line[:3] != f"{line_num}. ":
            return False
        line_num += 1
    return True

