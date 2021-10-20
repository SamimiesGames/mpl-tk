from abc import ABC, abstractmethod
from dataclasses import dataclass
from ..strproc import Strproc


@dataclass
class Token(ABC):
    label: str

    @abstractmethod
    def match(self, strproc: Strproc) -> bool:
        ...
