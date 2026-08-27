import pytest
from mercurytools.tree import Trie
from mercurytools.core.exceptions import ValueNotFoundError


def test_insert_and_search():
    trie=Trie()
    trie.insert("cat")
    trie.insert("car")
    assert trie.search("cat")
    assert trie.search("car")
    assert not trie.search("ca")
    assert not trie.search("dog")


def test_starts_with():
    trie=Trie()
    trie.insert("cat")
    assert trie.starts_with("ca")
    assert trie.starts_with("cat")
    assert not trie.starts_with("do")


def test_contains():
    trie=Trie()
    trie.insert("hello")
    assert "hello" in trie
    assert "hell" not in trie


def test_duplicate_insert_is_noop():
    trie=Trie()
    trie.insert("cat")
    trie.insert("cat")
    assert len(trie)==1


def test_remove():
    trie=Trie()
    trie.insert("cat")
    trie.insert("car")
    trie.remove("cat")
    assert not trie.search("cat")
    assert trie.search("car")
    assert len(trie)==1


def test_remove_not_found():
    trie=Trie()
    trie.insert("cat")
    with pytest.raises(ValueNotFoundError):
        trie.remove("dog")


def test_remove_prefix_only_raises():
    trie=Trie()
    trie.insert("cat")
    with pytest.raises(ValueNotFoundError):
        trie.remove("ca")


def test_words_with_prefix():
    trie=Trie()
    for w in ["cat","car","cart","dog"]:
        trie.insert(w)
    assert sorted(trie.words_with_prefix("ca"))==["car","cart","cat"]
    assert list(trie.words_with_prefix("do"))==["dog"]
    assert list(trie.words_with_prefix("xyz"))==[]


def test_iteration_sorted_order():
    trie=Trie()
    for w in ["banana","apple","cherry"]:
        trie.insert(w)
    assert list(trie)==["apple","banana","cherry"]


def test_clear():
    trie=Trie()
    trie.insert("cat")
    trie.clear()
    assert len(trie)==0
    assert not trie.search("cat")


def test_len_and_repr():
    trie=Trie()
    trie.insert("a")
    trie.insert("b")
    assert len(trie)==2
    assert "a" in repr(trie) and "b" in repr(trie)