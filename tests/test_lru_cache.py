from mercurytools.utils import LRUCache

def test_put_get():
    cache=LRUCache(2)
    cache.put("a",1)
    cache.put("b",2)
    assert cache.get("a")==1
    assert cache.get("b")==2


def test_eviction():
    cache=LRUCache(2)
    cache.put("a",1)
    cache.put("b",2)
    cache.put("c",3)
    assert cache.get("a") is None
    assert cache.get("b")==2
    assert cache.get("c")==3


def test_update_existing():
    cache=LRUCache(2)
    cache.put("a",1)
    cache.put("a",10)
    assert cache.get("a")==10
    assert len(cache)==1


def test_recent_usage():
    cache=LRUCache(2)
    cache.put("a",1)
    cache.put("b",2)
    cache.get("a")
    cache.put("c",3)
    assert cache.get("b") is None
    assert cache.get("a")==1
    assert cache.get("c")==3


def test_clear():
    cache=LRUCache(2)
    cache.put("a",1)
    cache.clear()
    assert len(cache)==0
    assert cache.get("a") is None