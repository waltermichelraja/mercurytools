"""fixed-capacity LRU [least-recently-used] cache."""


from ..core.nodes import LRUNode as Node


class LRUCache:
    """a fixed-capacity key/value cache that evicts the least recently used entry.
    both get() and put() count as "use" and move the entry to the front.
    Backed by a hash map [O(1) lookup] plus a doubly-linked list [O(1)
    reordering and eviction].
    """

    def __init__(self,capacity:int):
        """create a cache holding at most capacity entries."""
        if capacity<=0:
            raise ValueError("capacity must be greater than 0")
        self._capacity=capacity
        self._map={}
        self._head=None
        self._tail=None

    def __len__(self):
        return len(self._map)

    def __repr__(self):
        items=[]
        current=self._head
        while current:
            items.append(f"{current.key}:{current.value}")
            current=current.next
        return f"LRUCache({items})"


    def get(self,key):
        """return the value for key and mark it most recently used, or None if absent: O(1)."""
        node=self._map.get(key)
        if not node:
            return None
        self._move_to_head(node)
        return node.value

    def put(self,key,value):
        """insert or update key with value, marking it most recently used.
        if this insertion exceeds capacity, the least recently used
        entry is evicted: O(1).
        """
        node=self._map.get(key)
        if node:
            node.value=value
            self._move_to_head(node)
            return
        new_node=Node(key,value)
        self._map[key]=new_node
        self._add_to_head(new_node)
        if len(self._map)>self._capacity:
            self._evict()

    def clear(self):
        """remove all entries."""
        self._map.clear()
        self._head=None
        self._tail=None

    def keys(self):
        """yield keys from most to least recently used."""
        current=self._head
        while current:
            yield current.key
            current=current.next

    def values(self):
        """yield values from most to least recently used."""
        current=self._head
        while current:
            yield current.value
            current=current.next


    def _add_to_head(self,node):
        """insert node at the front [most recently used position]: O(1)."""
        node.prev=None
        node.next=self._head
        if self._head:
            self._head.prev=node
        self._head=node
        if not self._tail:
            self._tail=node

    def _remove_node(self,node):
        """unlink node from the list without touching the key map: O(1)."""
        if node.prev:
            node.prev.next=node.next
        else:
            self._head=node.next
        if node.next:
            node.next.prev=node.prev
        else:
            self._tail=node.prev

    def _move_to_head(self,node):
        """move an already-linked node to the front: O(1)."""
        self._remove_node(node)
        self._add_to_head(node)

    def _evict(self):
        """remove the least recently used entry (the tail) from both the list and the map: O(1)."""
        if not self._tail:
            return
        key=self._tail.key
        self._remove_node(self._tail)
        del self._map[key]