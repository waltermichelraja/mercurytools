import pytest
from mercurytools.disjoint_set import DisjointSet
from mercurytools.core.exceptions import ValueNotFoundError


def test_make_set_and_contains():
    ds=DisjointSet()
    ds.make_set("a")
    assert "a" in ds
    assert "b" not in ds


def test_make_set_noop_on_duplicate():
    ds=DisjointSet()
    ds.make_set("a")
    ds.make_set("a")
    assert len(ds)==1
    assert ds.num_sets==1


def test_find_returns_self_for_singleton():
    ds=DisjointSet()
    ds.make_set("a")
    assert ds.find("a")=="a"


def test_find_missing_raises():
    ds=DisjointSet()
    with pytest.raises(ValueNotFoundError):
        ds.find("missing")


def test_union_auto_creates_elements():
    ds=DisjointSet()
    ds.union("a","b")
    assert "a" in ds and "b" in ds
    assert ds.connected("a","b")


def test_union_merges_sets():
    ds=DisjointSet()
    ds.union("a","b")
    ds.union("b","c")
    assert ds.connected("a","c")
    assert ds.find("a")==ds.find("b")==ds.find("c")


def test_union_noop_if_already_connected():
    ds=DisjointSet()
    ds.union("a","b")
    before=ds.num_sets
    ds.union("a","b")
    assert ds.num_sets==before


def test_connected_false_for_different_sets():
    ds=DisjointSet()
    ds.make_set("a")
    ds.make_set("b")
    assert not ds.connected("a","b")


def test_connected_false_for_untracked_elements():
    ds=DisjointSet()
    assert not ds.connected("a","b")
    ds.make_set("a")
    assert not ds.connected("a","missing")


def test_size_of():
    ds=DisjointSet()
    ds.union("a","b")
    ds.union("b","c")
    ds.make_set("d")
    assert ds.size_of("a")==3
    assert ds.size_of("d")==1


def test_size_of_missing_raises():
    ds=DisjointSet()
    with pytest.raises(ValueNotFoundError):
        ds.size_of("missing")


def test_num_sets_decreases_on_union():
    ds=DisjointSet()
    for x in ["a","b","c","d"]:
        ds.make_set(x)
    assert ds.num_sets==4
    ds.union("a","b")
    assert ds.num_sets==3
    ds.union("c","d")
    assert ds.num_sets==2
    ds.union("a","c")
    assert ds.num_sets==1


def test_groups():
    ds=DisjointSet()
    ds.union("a","b")
    ds.union("c","d")
    ds.make_set("e")
    groups=[set(g) for g in ds.groups()]
    assert {"a","b"} in groups
    assert {"c","d"} in groups
    assert {"e"} in groups
    assert len(groups)==3


def test_clear():
    ds=DisjointSet()
    ds.union("a","b")
    ds.clear()
    assert len(ds)==0
    assert ds.num_sets==0
    assert "a" not in ds


def test_len_and_iter():
    ds=DisjointSet()
    ds.union("a","b")
    ds.make_set("c")
    assert len(ds)==3
    assert set(ds)=={"a","b","c"}


def test_repr():
    ds=DisjointSet()
    ds.union("a","b")
    r=repr(ds)
    assert "a" in r and "b" in r