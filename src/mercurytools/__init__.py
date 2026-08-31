"""mercurytools: a lightweight, consistent data structures library.

submodules:
    linear       -- LinkedList, Stack, Deque, PriorityQueue
    tree         -- BinaryTree, BinarySearchTree, AVLTree, Trie
    graph        -- Graph [adjacency list, BFS/DFS]
    disjoint_set -- DisjointSet [union-find]
    utils        -- LRUCache
"""


from . import linear
from . import utils
from . import tree
from . import graph
from . import disjoint_set
from .__version__ import __version__

__all__=["linear","utils","tree","graph","disjoint_set","__version__"]