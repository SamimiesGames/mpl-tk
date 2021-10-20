from dataclasses import dataclass
from ..strproc import Strproc
from ..profiling import Trace
from .token import Token


from typing import Union


@dataclass
class Lexer:
    strproc: Strproc
    tokens: list[Token]

    def match_token(self, trace: Trace) -> Union[None, Token]:
        """
        Linear search for correct token.

        :return: None if no valid token was found. Otherwise return Token

        **halts lexing if no valid token was found.**
        """
        for toke in self.tokens:
            is_toke = toke.match(self.strproc)

            if is_toke:
                return toke

        trace.halt()

    def tokenize(self):
        with self.strproc.join() as trace:
            self.match_token(trace)
