from mercurytools.linear import Stack

def test_push_pop():
    s=Stack()
    s.push(1)
    s.push(2)
    assert s.pop()==2
    assert s.pop()==1


def test_peek():
    s=Stack()
    s.push(10)
    assert s.peek()==10