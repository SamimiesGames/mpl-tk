from mpl import profiling
import pytest
from click import testing
import click

TRACE_CORRECT = """
Error(s) at trace-latest:
At <%s, line? %i word? %i>: [%s]
"""


@click.command()
def test_trace(name: str, line: int, word: int, outcome: str):
    trace = profiling.Trace()

    trace.put(profiling.Call(name, line, word, outcome))

    trace.throw()


@pytest.mark.parametrize(
    "name, line, word, outcome",
    [
        ("Label", 1, 1, "outcome")
    ]
)
def test_throw_trace_default_name(name: str, line: int, word: int, outcome: str):
    cli = testing.CliRunner()

    res = cli.invoke(test_trace, [name, line, word, outcome])

    trace_correct = TRACE_CORRECT % (name, line, word, outcome)

    assert res.output == trace_correct


if __name__ == '__main__':
    test_throw_trace_default_name()
