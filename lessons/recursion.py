"""Examples of recursion."""

from __future__ import annotations
from typing import Optional

class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Initializing the attributes of a Node."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Magic method to represent as a string."""
        if self.next == None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def sum(node: Optional[Node]) -> int:
    num_sum: int = 0
    while node != None:
        num_sum += node.data
        node = node.next
    return num_sum
    

def count(node: Optional[Node], current_count: int = 0) -> int:
    if node.next == None:
        return current_count
    else:
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)
