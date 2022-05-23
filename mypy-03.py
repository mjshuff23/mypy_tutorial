from typing import (
    Union, 
    Iterable, 
    Dict, 
    Callable, 
    Iterator, 
    cast, 
    Any, 
    Optional
)

def g(number: int) -> Iterator[int]:
    i = 0
    while i < number:
        yield i
        i +=1

g(5)

# An argument can be declared positional-only by giving it a name starting with two underscores:
def quux(__x: int) -> None:
    pass

quux(1)
# quux(__x=1) - Error: positional-only argument '__x'

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.

# reveal_type('hi') # mypy-03.py:21: note: Revealed type is "Literal['hi']?"

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
my_variable: Any = 'xadsfas'
# reveal_type(my_variable) # mypy-03.py:26: note: Revealed type is "Any"

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing a type annotation
my_list: list[str] = []
my_list_2: Optional[str] = None

# This makes each positional arg and each keyword arg a "str"
def called(self, *args: str, **kwargs: str) -> str:
    request = 'hi'
    return request

# Left off at https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#cheat-sheet-py3
