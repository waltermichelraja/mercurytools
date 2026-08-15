"""self-balancing [AVL] binary search tree."""


from ..core.base_tree import TreeBase
from ..core.nodes import BinaryTreeNode as Node
from ..core.exceptions import ValueNotFoundError


class AVLTree(TreeBase):
    """a self-balancing binary search tree with guaranteed O(log n) insert/remove/lookup.
    after every insert/remove, the tree rebalances via single or double
    rotations [LL, RR, LR, RL] so that for any node, its two child
    subtrees' heights never differ by more than 1.
    """

    def __contains__(self,value):
        """return True if value is present: O(log n)."""
        current=self._root
        while current:
            if value<current.data:
                current=current.left
            elif value>current.data:
                current=current.right
            else:
                return True
        return False

    def insert(self,data):
        """insert data, maintaining BST ordering and AVL balance: O(log n)."""
        self._set_root(self._insert(self._root,data))

    def _insert(self,node,data):
        """recursively insert data into the subtree rooted at node and rebalance;
        returns the new subtree root.
        """
        if not node:
            self._set_size(self._size+1)
            return Node(data)
        if data<node.data:
            node.left=self._insert(node.left,data)
        elif data>node.data:
            node.right=self._insert(node.right,data)
        else:
            return node
        self._update_height(node)
        return self._rebalance(node,data)

    def remove(self,value):
        """remove and return value, maintaining AVL balance: O(log n)."""
        new_root,deleted=self._remove(self._root,value)
        self._set_root(new_root)
        if deleted:
            self._set_size(self._size-1)
            return value
        raise ValueNotFoundError(f"{value} not found")

    def _remove(self,node,value):
        """recursively remove value from the subtree rooted at node and rebalance;
        returns [new_subtree_root, was_deleted].
        """
        if not node:
            return None,False
        if value<node.data:
            node.left,deleted=self._remove(node.left,value)
        elif value>node.data:
            node.right,deleted=self._remove(node.right,value)
        else:
            if not node.left:
                return node.right,True
            if not node.right:
                return node.left,True
            successor=self._min_node(node.right)
            node.data=successor.data
            node.right,deleted=self._remove(node.right,successor.data)
        self._update_height(node)
        return self._rebalance_after_delete(node),deleted

    def _min_node(self,node):
        """return the leftmost [smallest] node in the subtree rooted at node."""
        while node.left:
            node=node.left
        return node


    def _height(self,node):
        """return node's cached height, or 0 for None."""
        return node.height if node else 0

    def _balance(self,node):
        """return node's balance factor: left subtree height minus right subtree height."""
        return self._height(node.left)-self._height(node.right)

    def _update_height(self,node):
        """recompute and store node's height from its children's cached heights."""
        node.height=1+max(self._height(node.left),self._height(node.right))

    def _rebalance(self,node,data):
        """apply the appropriate rotation [if any] after inserting data below node."""
        balance=self._balance(node)
        if balance>1 and data<node.left.data:
            return self._rotate_right(node)
        if balance<-1 and data>node.right.data:
            return self._rotate_left(node)
        if balance>1 and data>node.left.data:
            node.left=self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance<-1 and data<node.right.data:
            node.right=self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rebalance_after_delete(self,node):
        """apply the appropriate rotation [if any] after a deletion below node."""
        balance=self._balance(node)
        if balance>1 and self._balance(node.left)>=0:
            return self._rotate_right(node)
        if balance>1 and self._balance(node.left)<0:
            node.left=self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance<-1 and self._balance(node.right)<=0:
            return self._rotate_left(node)
        if balance<-1 and self._balance(node.right)>0:
            node.right=self._rotate_right(node.right)
            return self._rotate_left(node)
        return node


    def _rotate_left(self,z):
        """left-rotate the subtree rooted at z; returns the new subtree root."""
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_right(self,z):
        """right-rotate the subtree rooted at z; returns the new subtree root."""
        y=z.left
        T3=y.right
        y.right=z
        z.left=T3
        self._update_height(z)
        self._update_height(y)
        return y
    
    def min(self):
        """return the smallest value, or None if empty: O(log n)."""
        if not self._root:
            return None
        node=self._root
        while node.left:
            node=node.left
        return node.data

    def max(self):
        """return the largest value, or None if empty: O(log n)."""
        if not self._root:
            return None
        node=self._root
        while node.right:
            node=node.right
        return node.data