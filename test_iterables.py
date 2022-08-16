"""Test iterables."""
from __future__ import annotations

import iterables


@iterables.iterable
class Items:
    """Class for testing iterables."""


def test_iterable():
    """Test iterable wrapper."""
    assert hasattr(Items(), "__iter__")
    assert hasattr(Items(), "__next__")
    assert hasattr(Items(), "__getitem__")
    assert hasattr(Items(), "__len__")
    assert hasattr(Items(), "__repr__")


def test_iterable_repr():
    """Test iterable repr."""
    assert repr(Items("a", "b")) == "Items('a', 'b')"


def test_iterable_iter():
    """Test iterable iter."""
    assert list(Items("a", "b")) == ["a", "b"]


def test_iterable_getitem():
    """Test iterable getitem."""
    assert Items("a", "b")[0] == "a"
    assert Items("a", "b")[1] == "b"


def test_iterable_append():
    """Test iterable append."""
    test = Items("a", "b")
    test.append("c")
    assert str(test) == "Items('a', 'b', 'c')"


def test_iterable_len():
    """Test iterable len."""
    assert len(Items("a", "b")) == 2
