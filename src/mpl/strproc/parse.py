from abc import ABC, abstractmethod
from dataclasses import dataclass


__all__ = [
    "Parser", "DefaultParser"
]


@dataclass
class Parser(ABC):

    @abstractmethod
    def parse(self, text_content: str) -> list[list[str]]:
        ...


class DefaultParser(Parser):
    def parse(self, text_content: str) -> list[list[str]]:
        lines = text_content.split("\n")
        fully_parsed = [line.split(" ") for line in lines]

        return fully_parsed
