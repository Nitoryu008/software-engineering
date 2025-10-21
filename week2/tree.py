from __future__ import annotations
from typing import Iterable, Iterator, List, Optional


class Tree(Iterable["Tree"]):
    def __init__(self, label: str, left: Optional[Tree], right: Optional[Tree]) -> None:
        self._label = label
        self._left = left
        self._right = right

    def __iter__(self) -> Iterator[Tree]:
        return _TreeIterator(self)


class _TreeIterator(Iterator[Tree]):
    def __init__(self, tree: Tree) -> None:
        self._stack: List[Tree] = []
        self._stack.append(tree)  # 木の根だけをスタックにpushしておく．

    def __next__(self) -> Tree:
        if len(self._stack) == 0:
            raise StopIteration

        node = self._stack.pop()  # これから調べるノードをスタックからpopする．

        if node._right:
            self._stack.append(node._right)

        if node._left:
            self._stack.append(node._left)

        return node  # 最初にスタックからpopしたノードを返す．
