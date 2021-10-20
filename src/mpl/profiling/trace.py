from dataclasses import dataclass, field
import click


@dataclass
class Call:
    label: str
    line: int
    word: int
    outcome: str

    def __str__(self):
        return f"At <{self.label}, line? {self.line} word? {self.word}>: [{self.outcome}]"


@dataclass
class Trace:
    queue: list[Call] = field(default_factory=list)
    label: str = "trace-latest"

    def put(self, call: Call):
        self.queue.append(call)

    def throw(self):
        click.secho(f"Error(s) in {self.label}:", fg="red")

        for call in self.queue:
            click.secho(f"{call}", fg="red")
