from dataclasses import dataclass
from ..strproc import Strproc
from .token import Token



@dataclass
class Lexer:
    strproc: Strproc
    tokens: list[Token]

    def tokenize(self):
        with self.strproc:
            ...
            # TODO: *
