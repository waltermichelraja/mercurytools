import pytest
from mercurytools.linear import Heap
from mercurytools.core.exceptions import EmptyStructureError


def test_min_heap_pop_order():
    h=Heap()
    for v in [5,1,4,2,3]:
        h.push(v)
    result=[h.pop() for _ in range(5)]
    assert result==[1,2,3,4,5]


def test_max_heap_pop_order():
    h=Heap(min_heap=False)
    for v in [5,1,4,2,3]:
        h.push(v)
    result=[h.pop() for _ in range(5)]
    assert result==[5,4,3,2,1]


def test_is_min_heap_flag():
    assert Heap().is_min_heap
    assert not Heap(min_heap=False).is_min_heap


def test_peek_does_not_remove():
    h=Heap()
    h.push(3)
    h.push(1)
    assert h.peek()==1
    assert len(h)==2


def test_peek_empty_returns_none():
    assert Heap().peek() is None


def test_pop_empty_raises():
    with pytest.raises(EmptyStructureError):
        Heap().pop()


def test_len():
    h=Heap()
    h.push(1)
    h.push(2)
    assert len(h)==2


def test_contains():
    h=Heap()
    h.push(1)
    h.push(2)
    assert 1 in h
    assert 99 not in h


def test_to_list_is_snapshot():
    h=Heap()
    h.push(3)
    h.push(1)
    lst=h.to_list()
    lst.append(999)
    assert 999 not in h


def test_clear():
    h=Heap()
    h.push(1)
    h.clear()
    assert len(h)==0
    assert h.peek() is None


def test_copy_is_independent():
    h=Heap()
    h.push(1)
    h.push(2)
    c=h.copy()
    c.push(3)
    assert len(h)==2
    assert len(c)==3
    assert h.pop()==1


def test_eq_ignores_internal_order():
    a=Heap()
    for v in [3,1,2]:
        a.push(v)
    b=Heap()
    for v in [1,2,3]:
        b.push(v)
    assert a==b


def test_eq_false_for_different_mode():
    a=Heap(min_heap=True)
    a.push(1)
    b=Heap(min_heap=False)
    b.push(1)
    assert a!=b


def test_eq_false_for_different_contents():
    a=Heap()
    a.push(1)
    b=Heap()
    b.push(2)
    assert a!=b


def test_eq_false_for_non_heap():
    h=Heap()
    h.push(1)
    assert h!=[1]


def test_from_iterable_min():
    h=Heap.from_iterable([5,3,8,1,9,2])
    result=[h.pop() for _ in range(6)]
    assert result==[1,2,3,5,8,9]


def test_from_iterable_max():
    h=Heap.from_iterable([5,3,8,1,9,2],min_heap=False)
    result=[h.pop() for _ in range(6)]
    assert result==[9,8,5,3,2,1]


def test_from_iterable_empty():
    h=Heap.from_iterable([])
    assert len(h)==0
    with pytest.raises(EmptyStructureError):
        h.pop()


def test_repr():
    h=Heap()
    h.push(1)
    r=repr(h)
    assert "min" in r and "1" in r