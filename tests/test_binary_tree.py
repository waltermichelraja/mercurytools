from mercurytools.tree import BinaryTree


def test_insert_and_level_order():
    bt=BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    assert list(bt.level_order())==[1,2,3]


def test_traversals():
    bt=BinaryTree()
    for i in range(1,6):
        bt.insert(i)
    assert list(bt.inorder())==[4,2,5,1,3]
    assert list(bt.preorder())==[1,2,4,5,3]
    assert list(bt.postorder())==[4,5,2,3,1]


def test_find():
    bt=BinaryTree()
    bt.insert(10)
    assert bt.find(10) is True
    assert bt.find(5) is False


def test_height():
    bt=BinaryTree()
    for i in range(7):
        bt.insert(i)
    assert bt.height()==2


def test_clear():
    bt=BinaryTree()
    bt.insert(1)
    bt.clear()
    assert len(bt)==0
    assert list(bt.level_order())==[]