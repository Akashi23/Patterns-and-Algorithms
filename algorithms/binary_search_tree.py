from typing import List


class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.data = None

class Queue:
    t: List[Node]
    front: int
    rear: int

    def __init__(self) -> None:
        self.t = []

