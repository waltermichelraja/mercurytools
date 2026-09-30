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

def test_equality_same_class():
    a,b=Stack(),Stack()
    for x in (1,2,3):
        a.push(x)
        b.push(x)
    assert a==b
    b.push(4)
    assert a!=b


def test_not_equal_to_other_linear_types():
    from mercurytools.linear import LinkedList,Deque
    s,ll,dq=Stack(),LinkedList(),Deque()
    for x in (1,2,3):
        s.push(x)
        ll.append(x)
        dq.append(x)
    assert s!=ll
    assert ll!=dq
    assert s!=dq
    assert s!=[1,2,3]