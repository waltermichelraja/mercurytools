class _Node:
    __slots__=("key","value","prev","next")

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:
    def __init__(self,capacity:int):
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
        node=self._map.get(key)
        if not node:
            return None
        self._move_to_head(node)
        return node.value

    def put(self,key,value):
        node=self._map.get(key)
        if node:
            node.value=value
            self._move_to_head(node)
            return
        new_node=_Node(key,value)
        self._map[key]=new_node
        self._add_to_head(new_node)
        if len(self._map)>self._capacity:
            self._evict()

    def clear(self):
        self._map.clear()
        self._head=None
        self._tail=None

    def keys(self):
        current=self._head
        while current:
            yield current.key
            current=current.next

    def values(self):
        current=self._head
        while current:
            yield current.value
            current=current.next


    def _add_to_head(self,node):
        node.prev=None
        node.next=self._head
        if self._head:
            self._head.prev=node
        self._head=node
        if not self._tail:
            self._tail=node

    def _remove_node(self,node):
        if node.prev:
            node.prev.next=node.next
        else:
            self._head=node.next
        if node.next:
            node.next.prev=node.prev
        else:
            self._tail=node.prev

    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_to_head(node)

    def _evict(self):
        if not self._tail:
            return
        key=self._tail.key
        self._remove_node(self._tail)
        del self._map[key]