"""adjacency-list graph, directed or undirected, with optional edge weights."""


from __future__ import annotations
from collections.abc import Hashable
from typing import Any, Dict, Generic, Iterator, Optional, TypeVar

from ..core.exceptions import ValueNotFoundError

V=TypeVar("V",bound=Hashable)


class Graph(Generic[V]):
    """a graph backed by an adjacency list [vertex -> {neighbor: weight}].
    directed/undirected is fixed at construction; edges without an
    explicit weight are stored with weight None. len(graph) and
    __iter__ operate over vertices [in insertion order]; edge_count
    tracks the number of distinct edges [each undirected edge counts
    once, not twice].
    """

    def __init__(self,directed:bool=False) -> None:
        self._adj:Dict[V,Dict[V,Optional[Any]]]={}
        self._directed:bool=directed
        self._edge_count:int=0

    @property
    def directed(self) -> bool:
        """True if this graph treats edges as one-directional."""
        return self._directed

    @property
    def edge_count(self) -> int:
        """number of distinct edges."""
        return self._edge_count

    def __len__(self) -> int:
        return len(self._adj)

    def __iter__(self) -> Iterator[V]:
        """iterate over vertices in insertion order."""
        return iter(self._adj)

    def __contains__(self,vertex:V) -> bool:
        """return True if vertex is present: O(1)."""
        return vertex in self._adj

    def __repr__(self) -> str:
        kind="directed" if self._directed else "undirected"
        return f"{self.__class__.__name__}({kind}, vertices={list(self._adj)})"


    def add_vertex(self,vertex:V) -> None:
        """add vertex with no edges. a no-op if vertex is already present: O(1)."""
        if vertex not in self._adj:
            self._adj[vertex]={}

    def add_edge(self,u:V,v:V,weight:Optional[Any]=None) -> None:
        """add an edge between u and v, creating either vertex if missing.
        for a directed graph this adds only u -> v; for an undirected
        graph it adds both directions. re-adding an existing edge
        overwrites its weight without changing edge_count: O(1).
        """
        self.add_vertex(u)
        self.add_vertex(v)
        is_new=v not in self._adj[u]
        self._adj[u][v]=weight
        if not self._directed:
            self._adj[v][u]=weight
        if is_new:
            self._edge_count+=1

    def has_vertex(self,vertex:V) -> bool:
        """return True if vertex is present: O(1)."""
        return vertex in self._adj

    def has_edge(self,u:V,v:V) -> bool:
        """return True if an edge from u to v exists: O(1)."""
        return u in self._adj and v in self._adj[u]

    def weight(self,u:V,v:V) -> Optional[Any]:
        """return the weight of the edge from u to v [None if unweighted].
        raises ValueNotFoundError if the edge doesn't exist: O(1).
        """
        if not self.has_edge(u,v):
            raise ValueNotFoundError(f"edge {u!r} -> {v!r} not found")
        return self._adj[u][v]

    def neighbors(self,vertex:V) -> Iterator[V]:
        """yield vertex's neighbors, in insertion order.
        raises ValueNotFoundError if vertex isn't present.
        """
        if vertex not in self._adj:
            raise ValueNotFoundError(f"{vertex!r} not found")
        yield from self._adj[vertex]

    def degree(self,vertex:V) -> int:
        """return the number of vertex's neighbors [out-degree for directed graphs]: O(1)."""
        if vertex not in self._adj:
            raise ValueNotFoundError(f"{vertex!r} not found")
        return len(self._adj[vertex])

    def remove_edge(self,u:V,v:V) -> None:
        """remove the edge from u to v [both directions if undirected]: O(1)."""
        if not self.has_edge(u,v):
            raise ValueNotFoundError(f"edge {u!r} -> {v!r} not found")
        del self._adj[u][v]
        if not self._directed and u in self._adj[v]:
            del self._adj[v][u]
        self._edge_count-=1

    def remove_vertex(self,vertex:V) -> V:
        """remove vertex and every edge touching it: O(V) [scans
        every other vertex's adjacency for incoming edges].
        """
        if vertex not in self._adj:
            raise ValueNotFoundError(f"{vertex!r} not found")
        self._edge_count-=len(self._adj[vertex])
        del self._adj[vertex]
        for neighbors in self._adj.values():
            if vertex in neighbors:
                del neighbors[vertex]
                if self._directed:
                    self._edge_count-=1
        return vertex

    def clear(self) -> None:
        """remove all vertices and edges."""
        self._adj={}
        self._edge_count=0


    def bfs(self,start:V) -> Iterator[V]:
        """yield vertices reachable from start in breadth-first order, each exactly once: O(V + E)."""
        if start not in self._adj:
            raise ValueNotFoundError(f"{start!r} not found")
        visited={start}
        queue=[start]
        i=0
        while i<len(queue):
            current=queue[i]
            i+=1
            yield current
            for neighbor in self._adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self,start:V) -> Iterator[V]:
        """yield vertices reachable from start in depth-first order, each exactly once.
        iterative [no recursion depth limit]: O(V + E).
        """
        if start not in self._adj:
            raise ValueNotFoundError(f"{start!r} not found")
        visited={start}
        stack=[start]
        while stack:
            current=stack.pop()
            yield current
            for neighbor in reversed(list(self._adj[current])):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)