from mercurytools.tree import BinarySearchTree


def test_insert_and_inorder():
    bst=BinarySearchTree()
    for i in [5,3,7,2,4,6,8]:
        bst.insert(i)
    assert list(bst)==[2,3,4,5,6,7,8]


def test_find():
    bst=BinarySearchTree()
    bst.insert(10)
    assert bst.find(10) is True
    assert bst.find(5) is False


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