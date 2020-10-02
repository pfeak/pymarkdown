import platform
from enum import Enum, unique


@unique
class Type(Enum):
    """Markdown type
    """
    # Place holder
    NULL = ""
    SPACE = " "

    # Markdown single symbol
    H1 = "#"
    H2 = "##"
    H3 = "###"
    H4 = "####"
    H5 = "#####"
    H6 = "######"
    QUOTE = ">"
    UNORDERED_LIST = "+"

    # Markdown double symbol
    BOLD = "**"
    STRIKETHROUGH = "~~"

    # Special symbol
    SPLIT_LINE = "---"
    IMAGE = '![REPLACE_ALT](REPLACE_URL REPLACE_TITLE)'
    URL = '[REPLACE_TITLE](REPLACE_URL)'
    ORDERED_LIST = "REPLACE_NUMBER."

    # Separation
    SEP = '\n'
