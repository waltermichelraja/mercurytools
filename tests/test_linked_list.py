from mercurytools import LinkedList


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