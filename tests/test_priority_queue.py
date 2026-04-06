import pytest
from mercurytools import PriorityQueue


def test_basic_push_pop():
    pq=PriorityQueue()
    pq.push(3)
    pq.push(1)
    pq.push(2)
    assert pq.pop()==1
    assert pq.pop()==2
    assert pq.pop()==3


def test_peek():
    pq=PriorityQueue()
    pq.push(10)
    pq.push(5)
    assert pq.peek()==5
    assert len(pq)==2


def test_len():
    pq=PriorityQueue()
    pq.push(1)
    pq.push(2)
    assert len(pq)==2


def test_to_list():
    pq=PriorityQueue()
    pq.push(3)
    pq.push(1)
    pq.push(2)
    result=pq.to_list()
    assert set(result)=={1,2,3}


def test_priority_mode_order():
    pq=PriorityQueue()
    pq.push("low",priority=3)
    pq.push("high",priority=1)
    pq.push("medium",priority=2)
    assert pq.pop()=="high"
    assert pq.pop()=="medium"
    assert pq.pop()=="low"


def test_priority_stability():
    pq=PriorityQueue()
    pq.push("a",priority=1)
    pq.push("b",priority=1)
    pq.push("c",priority=1)
    assert pq.pop()=="a"
    assert pq.pop()=="b"
    assert pq.pop()=="c"


def test_mixing_priority_and_non_priority():
    pq=PriorityQueue()
    pq.push(1)
    with pytest.raises(ValueError):
        pq.push(2,priority=1)


def test_reverse_mixing_priority_and_non_priority():
    pq=PriorityQueue()
    pq.push(1,priority=1)
    with pytest.raises(ValueError):
        pq.push(2)


def test_pop_empty():
    pq=PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_empty():
    pq=PriorityQueue()
    assert pq.peek() is None


def test_non_comparable_values():
    pq=PriorityQueue()
    pq.push(1)
    with pytest.raises(TypeError):
        pq.push("string")
