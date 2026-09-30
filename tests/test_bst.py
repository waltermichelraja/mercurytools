from mercurytools.tree import BinarySearchTree


def test_insert_and_inorder():
    bst=BinarySearchTree()
    for i in [5,3,7,2,4,6,8]:
        bst.insert(i)
    assert list(bst)==[2,3,4,5,6,7,8]


def test_remove_leaf():
    bst=BinarySearchTree()
    for i in [5,3,7]:
        bst.insert(i)
    bst.remove(3)
    assert list(bst)==[5,7]


def test_remove_one_child():
    bst=BinarySearchTree()
    for i in [5,3,7,6]:
        bst.insert(i)
    bst.remove(7)
    assert list(bst)==[3,5,6]


def test_remove_two_children():
    bst=BinarySearchTree()
    for i in [5,3,7,2,4,6,8]:
        bst.insert(i)
    bst.remove(5)
    assert list(bst)==[2,3,4,6,7,8]


def test_remove_not_found():
    bst=BinarySearchTree()
    bst.insert(1)
    try:
        bst.remove(2)
    except ValueError:
        assert True

import random
import pytest
from mercurytools.core.exceptions import ValueNotFoundError


def _reference_traversals(values):
    """recursive reference traversals over a BST built by mercurytools, for comparison."""
    def pre(n): return [] if not n else [n.data]+pre(n.left)+pre(n.right)
    def post(n): return [] if not n else post(n.left)+post(n.right)+[n.data]
    return pre,post


def test_traversals_match_recursive_reference():
    rng=random.Random(1)
    for _ in range(30):
        bst=BinarySearchTree()
        vals=rng.sample(range(200),rng.randint(0,60))
        for v in vals:
            bst.insert(v)
        pre,post=_reference_traversals(vals)
        assert list(bst.inorder())==sorted(vals)
        assert list(bst.preorder())==pre(bst.root)
        assert list(bst.postorder())==post(bst.root)


def test_deep_degenerate_tree_does_not_hit_recursion_limit():
    bst=BinarySearchTree()
    for i in range(5000):  # sorted insertion => a 5000-deep chain
        bst.insert(i)
    assert len(list(bst.inorder()))==5000
    assert len(list(bst.preorder()))==5000
    assert len(list(bst.postorder()))==5000
    assert bst.height()==4999
    assert bst.remove(4999)==4999
    assert bst.remove(0)==0
    assert len(bst)==4998


def test_remove_matches_set_model():
    rng=random.Random(2)
    for _ in range(40):
        bst,model=BinarySearchTree(),set()
        for _ in range(120):
            v=rng.randint(0,40)
            if rng.random()<0.55:
                bst.insert(v)
                model.add(v)
            elif v in model:
                assert bst.remove(v)==v
                model.remove(v)
            else:
                with pytest.raises(ValueNotFoundError):
                    bst.remove(v)
            assert list(bst)==sorted(model)
            assert len(bst)==len(model)


def test_remove_root_with_two_children_and_single_node():
    bst=BinarySearchTree()
    for v in [5,3,8,7,9]:
        bst.insert(v)
    bst.remove(5)
    assert list(bst)==[3,7,8,9]
    assert bst.root.data==7
    single=BinarySearchTree()
    single.insert(1)
    single.remove(1)
    assert single.root is None and len(single)==0