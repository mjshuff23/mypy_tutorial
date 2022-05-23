def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print(f"Hello {name}")

friends1 = ['Michael', 'Bob', 'Alice']
friends2 = ('Michael', 'Bob', 'Alice')

greet_all(friends1)
greet_all(friends2)

# As another example, suppose you want to write a function that can accept either ints or strings, but no other types. You can express this using the Union type:
from typing import Union, Iterable, Dict

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id

print(normalize_id(12451251))
print(normalize_id('12451251'))

# Similarly, suppose that you want the function to accept only strings or None. You can again use Union and use Union[str, None] – or alternatively, use the type Optional[str]. These two types are identical and interchangeable: Optional[str] is just a shorthand or alias for Union[str, None]. It exists mostly as a convenience to help function signatures look a little cleaner:

from typing import Optional

def greeting(name: Optional[str] = None) -> str:
    # Optional[str] is shorthand for Union[str, None]
    if name is None:
        name = 'stranger'
    return f"Hello, {name}"

print(greeting())
print(greeting('Michael'))

# Type inference - By default, mypy infers types for you. You can instruct mypy to infer types for you by adding type annotations. For example, you can tell mypy that a function returns a string like so:
def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output = []
    for number in numbers:
        if number < limit:
            output.append(number)
    return output

print(nums_below((1.0, 2.0, 3.0, 4.0, 5.0), 3.0))

# Mypy will warn you if it is unable to determine the type of some variable – for example, when assigning an empty dictionary to some global value:
# my_global_dict = {} # Error: Need type annotation for 'my_global_dict'
my_global_dict: dict[int, float] = {}

# You can teach mypy what type my_global_dict is meant to have by giving it a type hint. For example, if you knew this variable is supposed to be a dict of ints to floats, you could annotate it using either variable annotations (introduced in Python 3.6 by PEP 526) or using a comment-based syntax like so:

#  Python 3.9+
my_global_dict_2: dict[int, float] = {}

# Python 3.6+
my_global_dict_3: Dict[int, float] = {}

# If you want compatibility with even older versions of Python
my_global_dict_4 = {} # type: Dict[int, float]

