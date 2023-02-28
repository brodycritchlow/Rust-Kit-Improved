"""
IMPLEMENTED BY RUSTKIT IMPROVED (R)
"""

from typing import TypeVar, List, Optional
import typing

T = TypeVar('T')

class Vector:
    """
    A generic vector class that stores elements of a single type.

    Examples:
        Create an empty vector and add some items to it:

        >>> v = Vector()
        >>> v.push(1)
        >>> v.push(2)
        >>> v.push(3)
        >>> len(v)
        3
        >>> v.pop()
        3
        >>> v[0]
        1
        >>> v[1] = 4
        >>> v[1]
        4
    """

    def __init__(self) -> None:
        """
        Initialize an empty vector.
        """
        self._items: List[T] = []
        self.type = type

    def push(self, item: T) -> None:
        """
        Add an item to the end of the vector.

        Args:
            item: The item to add.

        Returns:
            None

        Examples:
            >>> v = Vector()
            >>> v.push(1)
            >>> v.push(2)
            >>> len(v)
            2
        """
        if type(item) != self.type and self.type != None:
            raise TypeError(f"{self} only supports {self.type} values, you provided {type(item)}")
        
        self._items.append(item)

    def pop(self) -> T:
        """
        Remove and return the last item in the vector.

        Returns:
            The last item in the vector.

        Raises:
            IndexError: If the vector is empty.

        Examples:
            >>> v = Vector()
            >>> v.push(1)
            >>> v.push(2)
            >>> v.push(3)
            >>> v.pop()
            3
        """
        return self._items.pop()

    def __len__(self) -> int:
        """
        Return the number of items in the vector.

        Returns:
            The number of items in the vector.

        Examples:
            >>> v = Vector()
            >>> v.push(1)
            >>> v.push(2)
            >>> len(v)
            2
        """
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        """
        Return the item at the given index.

        Args:
            index: The index of the item to return.

        Returns:
            The item at the given index.

        Raises:
            IndexError: If the index is out of range.

        Examples:
            >>> v = Vector()
            >>> v.push(1)
            >>> v.push(2)
            >>> v.push(3)
            >>> v[1]
            2
        """
        
        if isinstance(index, type):
            self.type = index
            return self
        elif index is typing.Any:
            self.type = None
            return self
        
        return self._items[index]
