from mercurytools.linear import LinkedList

def test_append():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.to_list()==[1,2]


def test_prepend():
    ll=LinkedList()
    ll.prepend(1)
    ll.prepend(0)
    assert ll.to_list()==[0,1]


def test_insert():
    ll=LinkedList()
    ll.append(1)
    ll.append(3)
    ll.insert(1,2)
    assert ll.to_list()==[1,2,3]


def test_remove():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove(1)
    assert ll.to_list()==[2]


def test_reverse():
    ll=LinkedList()
    for i in range(5):
        ll.append(i)
    ll.reverse()
    assert ll.to_list()==[4,3,2,1,0]


def test_copy():
    ll=LinkedList()
    ll.append(1)
    copy=ll.copy()
    assert copy==ll

def test_slice():
    ll=LinkedList()
    for i in range(5):
        ll.append(i)
    assert ll[1:4].to_list()==[1,2,3]


def test_reverse_iter():
    ll=LinkedList()
    for i in range(3):
        ll.append(i)
    assert list(reversed(ll))==[2,1,0]


def test_extend():
    ll=LinkedList()
    ll.extend([1,2,3])
    assert ll.to_list()==[1,2,3]


def test_pop_index():
    ll=LinkedList()
    ll.extend([1,2,3])
    assert ll.pop(1)==2
    assert ll.to_list()==[1,3]

def test_slice_positive_step():
    ll=LinkedList()
    ll.extend([0,1,2,3,4,5])
    assert ll[1:5:2].to_list()==[1,3]
    assert ll[:3].to_list()==[0,1,2]


def test_slice_negative_step_reverses():
    ll=LinkedList()
    ll.extend([1,2,3])
    assert ll[::-1].to_list()==[3,2,1]
    assert ll[::-2].to_list()==[3,1]
    assert ll[2:0:-1].to_list()==[3,2]


def test_slice_matches_builtin_list_semantics():
    data=list(range(10))
    ll=LinkedList()
    ll.extend(data)
    for s in [slice(None,None,-1),slice(7,2,-2),slice(-1,None,-3),slice(2,8,3),slice(20,30),slice(None,None,None)]:
        assert ll[s].to_list()==data[s]


def test_slice_returns_independent_copy():
    ll=LinkedList()
    ll.extend([1,2,3])
    sliced=ll[::-1]
    sliced.append(99)
    assert ll.to_list()==[1,2,3]