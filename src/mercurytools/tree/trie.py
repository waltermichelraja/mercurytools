"""prefix tree [trie] for storing and querying strings."""


from __future__ import annotations
from typing import Iterator, Optional

from ..core.nodes import TrieNode
from ..core.exceptions import ValueNotFoundError


class Trie:
    """a prefix tree storing strings, with O(m) insert/search/prefix lookups
    where m is the length of the string involved. unlike the other tree
    types in this library, Trie always stores str and is not generic --
    its structure is defined by character-by-character branching, so a
    type parameter would not add anything.
    """

    def __init__(self) -> None:
        self._root:TrieNode=TrieNode()
        self._size:int=0

    @property
    def size(self) -> int:
        """number of complete words currently stored."""
        return self._size

    def __len__(self) -> int:
        return self._size

    def __contains__(self,word:str) -> bool:
        """return True if word was inserted as a complete word [not just a prefix]: O(m)."""
        return self.search(word)

    def __iter__(self) -> Iterator[str]:
        """yield all stored words in sorted [lexicographic] order."""
        yield from self._collect(self._root,"")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"


    def insert(self,word:str) -> None:
        """insert word. inserting an already-present word is a no-op: O(m)."""
        node=self._root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        if not node.is_end:
            node.is_end=True
            self._size+=1

    def search(self,word:str) -> bool:
        """return True if word was inserted as a complete word: O(m)."""
        node=self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self,prefix:str) -> bool:
        """return True if any inserted word begins with prefix: O(m)."""
        return self._find_node(prefix) is not None

    def remove(self,word:str) -> str:
        """remove word.
        raises ValueNotFoundError if word was not inserted as a complete
        word [including if it exists only as a prefix of longer words]: O(m).
        """
        node=self._find_node(word)
        if node is None or not node.is_end:
            raise ValueNotFoundError(f"{word} not found")
        node.is_end=False
        self._size-=1
        return word

    def words_with_prefix(self,prefix:str) -> Iterator[str]:
        """yield all stored words that begin with prefix, in sorted order:
        O(m + k) where k is the size of the matching subtree.
        """
        node=self._find_node(prefix)
        if node is None:
            return
        yield from self._collect(node,prefix)

    def clear(self) -> None:
        """remove all words."""
        self._root=TrieNode()
        self._size=0


    def _find_node(self,word:str) -> Optional[TrieNode]:
        """walk the trie along word's characters; return the final node, or None if the path breaks."""
        node=self._root
        for ch in word:
            if ch not in node.children:
                return None
            node=node.children[ch]
        return node

    def _collect(self,node:TrieNode,prefix:str) -> Iterator[str]:
        """yield all complete words in the subtree rooted at node, each prefixed by prefix, in sorted order."""
        if node.is_end:
            yield prefix
        for ch in sorted(node.children):
            yield from self._collect(node.children[ch],prefix+ch)