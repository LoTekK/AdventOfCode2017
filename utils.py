from pathlib import Path
from contextlib import contextmanager


@contextmanager
def get_input(day):
    f = open(Path(f'.\\{day}input.txt'), mode='r')
    try:
        yield f
    finally:
        f.close()
