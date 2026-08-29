"""mercurytools: a lightweight, consistent data structures library.

submodules:
    linear -- LinkedList, Stack, Deque, PriorityQueue
    tree   -- BinaryTree, BinarySearchTree, AVLTree, Trie
    graph  -- Graph [adjacency list, BFS/DFS]
    utils  -- LRUCache
"""


from . import linear
from . import utils
from . import tree
from . import graph
from .__version__ import __version__

__all__=["linear","utils","tree","graph","__version__"]