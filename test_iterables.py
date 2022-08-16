"""Test iterables."""
from __future__ import annotations

import iterables


@iterables.iterable
class Test:
    """Class for testing iterables."""


def test_iterable():
    """Test iterable wrapper."""
    assert hasattr(Test(), "__iter__")
    assert hasattr(Test(), "__next__")
    assert hasattr(Test(), "__getitem__")
    assert hasattr(Test(), "__len__")
    assert hasattr(Test(), "__repr__")


def test_iterable_repr():
    """Test iterable repr."""
    assert repr(Test("a", "b")) == "Test('a', 'b')"


def test_iterable_iter():
    """Test iterable iter."""
    assert list(Test("a", "b")) == ["a", "b"]


def test_iterable_getitem():
    """Test iterable getitem."""
    assert Test("a", "b")[0] == "a"
    assert Test("a", "b")[1] == "b"


def test_iterable_append():
    """Test iterable append."""
    test = Test("a", "b")
    test.append("c")
    assert str(test) == "Test('a', 'b', 'c')"


def test_iterable_len():
    """Test iterable len."""
    assert len(Test("a", "b")) == 2
