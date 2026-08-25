"""
Lab 1: The Typed Script -- TypedContainer starter.

Complete TypedContainer below. See the assignment, Part B,
for the full requirements. Do not rename the class or its methods --
test_container.py imports them by name.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class TypedContainer(Generic[T]):
    """A strictly-typed key-value container. Keys must always be str."""

    def __init__(self) -> None:
        # DONE_TODO: set up your internal storage (e.g. a dict).
        self.data: dict[str, T] = {}
        #raise NotImplementedError

    def set(self, key: str, value: T) -> None:
        """
        Store `value` under `key`.

        Must raise TypeError immediately if `key` is not a str --
        no silent coercion. See Part A, Question 3, for why.
        """
        # DONE_TODO
        #raise NotImplementedError
        if not isinstance(key, str):
            raise TypeError("key not string")
        self.data[key] = value

    def get(self, key: str) -> T:
        """
        Return the value stored under `key`.

        Must raise TypeError immediately if `key` is not a str.
        """
        # Done_TODO
        #raise NotImplementedError
        if not isinstance(key, str):
            raise TypeError("key not str")
        return self.data[key]

    def __contains__(self, key: str) -> bool:
        # DONE_TODO: support the `in` operator.
        if not isinstance(key, str):
            raise TypeError("key not str")
        return key in self.data
        #raise NotImplementedError

    def __len__(self) -> int:
        # DONE_TODO: support len(container).
        return len(self.data)
        #raise NotImplementedError
