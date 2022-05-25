# You can teach mypy to detect these kinds of bugs by adding type annotations (also known as type hints). For example, you can teach mypy that greeting both accepts and returns a string like so:
def greeting(name: str) -> str:
    return f"Hello, {name}!"

def addition(x: int, y: int) -> int:
    return x + y

print(greeting("Michael"))

# If a function does not explicitly return a value, give it a return type of None. Using a None result in a statically typed context results in a type check error:
def p() -> None:
    print("Hello")

# a = p() # Error: p() does not return a value

# Arguments with default values can be annotated like so:
def greetings(name: str = "World", excited: bool = False) -> str:
    message = 'Hello, {}'.format(name)
    if excited:
        message += "!!!"
    return message

print(greetings(excited=True))

def second_addition(x: int = 5, y: int = 10) -> int:
    return x + y

print(second_addition())

# *args and **kwargs arguments can be annotated like so:
def stars(*args: int, **kwargs: float) -> None:
    # 'args' has type 'tuple[int, ...] (a tuple of ints)
    # 'kwargs' has type 'dict[str, float] (a dict of str to float)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

stars(1, 2, 3, a=1.0, b=2.0)

# to indicate that some function can accept a list of strings, use the list[str] type
def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)
    
names = ['Michael', 'Bob', 'Alice']
ages = [25, 30, 35]

greet_all(names)

