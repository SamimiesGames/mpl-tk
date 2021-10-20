from abc import ABC, abstractmethod
from dataclasses import dataclass
from contextlib import contextmanager

from ..profiling import Trace, Call


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
    def join(self) -> Trace:
        trace = Trace()
        try:
            for line in self.lines:
                trace.put(Call(f"Scanline", self.line, self.word, f"{' '.join(line)}"))
                for word in line:
                    trace.put(Call("Scanword", self.line, self.word, word))
                    self.word += 1

                    yield trace

                    if trace.latest_call_failed:
                        break

                if trace.latest_call_failed:
                    break

                self.line += 1
                self.word = 0
        finally:
            if trace.latest_call_failed:
                trace.throw()
