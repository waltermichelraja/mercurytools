from mercurytools.tree import AVLTree


def test_balancing():
    avl=AVLTree()
    for i in [10,20,30]:
        avl.insert(i)
    assert list(avl)==[10,20,30]
    assert avl.height()==1


def test_insert_many():
    avl=AVLTree()
    for i in range(10):
        avl.insert(i)
    assert sorted(list(avl))==list(range(10))


def test_remove():
    avl=AVLTree()
    for i in [10,20,30,40,50]:
        avl.insert(i)
    avl.remove(30)
    assert 30 not in avl