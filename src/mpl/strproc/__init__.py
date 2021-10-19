from .strproc import *
from .parse import *
from .file import *


def create_strproc(filename: str, parser: Parser, proc: Strproc) -> Strproc:
    text_content = read_file(filename)
    parsed = parser.parse(text_content)
    return proc(parsed)
