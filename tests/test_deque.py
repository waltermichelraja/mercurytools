from mercurytools import Deque


def test_append_pop():
    d=Deque()
    d.append(1)
    d.append(2)
    assert d.pop()==2


def test_appendleft_popleft():
    d=Deque()
    d.appendleft(1)
    d.appendleft(2)
    assert d.popleft()==2