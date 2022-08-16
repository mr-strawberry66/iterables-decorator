# Iterable decorator
Create iterable classes using a class decorator.

Values added to an iterable class are sored in the class's `self.args` attribute as a `tuple` of whatever type you have provided.

## Example
```python
from iterables import iterable

@iterable
class Items:

    # You can type annotate your iterable like so:
    item: str
    # Note that this has no real effect on the generation of the iterable.

items = Items("Hello", "iterables!")

for item in items:
    print(item)

>>> "Hello"
>>> "iterables!"
```
