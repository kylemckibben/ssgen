def extract_title(markdown: str) -> str:
    """Get heading 1 title from markdown document

    Arguments:
    markdown -- markdown file
    """
    if markdown[0] != '#' and markdown[1] != ' ':
        raise Exception('ERROR: missing document title')
    title: str = ""
    idx = 2
    while markdown[idx] != '\n':
        title += markdown[idx]
        idx += 1

    return title

