from abc import ABC, abstractmethod
from dataclasses import dataclass
from contextlib import contextmanager


__all__ = [
    "Strproc", "BasicStrproc"
]


@dataclass
class Strproc(ABC):
    lines: list[list[str]]

    line: int = 0
    word: int = 0

    @abstractmethod
    @contextmanager
    def join(self) -> None:
        ...


class BasicStrproc(Strproc):
    @contextmanager
    def join(self):
        try:
            for line in self.lines:
                for word in line:
                    self.word += 1
                    yield

                self.line += 1
                self.word = 0
        finally:
            ...
