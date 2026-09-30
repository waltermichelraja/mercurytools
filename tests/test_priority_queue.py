import pytest
from mercurytools.linear import PriorityQueue


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


def test_failed_push_leaves_queue_unchanged():
    pq=PriorityQueue()
    for v,p in [("a",1),("b",2),("c",3)]:
        pq.push(v,p)
    with pytest.raises(TypeError):
        pq.push("x","not-a-number")
    assert len(pq)==3
    assert [pq.pop() for _ in range(3)]==["a","b","c"]


def test_failed_push_does_not_consume_tiebreak_counter():
    pq=PriorityQueue()
    pq.push("first",1)
    with pytest.raises(TypeError):
        pq.push("bad","x")
    pq.push("second",1)
    pq.push("third",1)
    assert [pq.pop() for _ in range(3)]==["first","second","third"]


def test_failed_first_push_in_mixed_mode_does_not_lock_mode():
    pq=PriorityQueue()
    pq.push("a",1)
    with pytest.raises(ValueError):
        pq.push("b")  # mixing modes
    assert len(pq)==1
    pq.pop()
    pq.clear()
    pq.push("z")  # mode reset after clear()
    assert pq.pop()=="z"


def test_push_pop_matches_sorted_reference():
    import random
    rng=random.Random(3)
    pq=PriorityQueue()
    items=[(f"v{i}",rng.randint(0,15)) for i in range(200)]
    for v,p in items:
        pq.push(v,p)
    expected=[v for v,_ in sorted(items,key=lambda t:t[1])]  # stable => FIFO ties
    assert [pq.pop() for _ in range(len(items))]==expected