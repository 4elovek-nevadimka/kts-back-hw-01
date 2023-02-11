from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = list()
        self.dfs_go(self._root, visited)
        return visited

    def dfs_go(self, node: Node, visited: list[Node]):
        if node not in visited:
            visited.append(node)
            for outboundNode in node.outbound:
                self.dfs_go(outboundNode, visited)

    def bfs(self) -> list[Node]:
        visited = list()
        queue = list()

        visited.append(self._root)
        queue.append(self._root)

        while queue:
            node = queue.pop(0)

            for outboundNode in node.outbound:
                if outboundNode not in visited:
                    visited.append(outboundNode)
                    queue.append(outboundNode)

        return visited
