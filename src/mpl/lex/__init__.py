from dataclasses import dataclass


@dataclass
class Lexer:
    text_content: list[list[str]]
