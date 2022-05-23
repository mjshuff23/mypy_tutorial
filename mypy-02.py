from collections.abc import Iterable # or 'from typing import Iterable'

def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print(f"Hello {name}")

friends1 = ['Michael', 'Bob', 'Alice']
friends2 = ('Michael', 'Bob', 'Alice')

greet_all(friends1)
greet_all(friends2)

# As another example, suppose you want to write a function that can accept either ints or strings, but no other types. You can express this using the Union type:
from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id

print(normalize_id(12451251))
print(normalize_id('12451251'))