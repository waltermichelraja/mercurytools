"""mercurytools: a lightweight, consistent data structures library.

submodules:
    linear -- LinkedList, Stack, Deque, PriorityQueue
    tree   -- BinaryTree, BinarySearchTree, AVLTree
    utils  -- LRUCache
"""


from . import linear
from . import utils
from . import tree
from .__version__ import __version__

__all__=["linear","utils","tree","__version__"]