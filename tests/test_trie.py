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

def _node_count(trie):
    def count(n): return 1+sum(count(c) for c in n.children.values())
    return count(trie._root)


def test_remove_prunes_dead_branch():
    trie=Trie()
    trie.insert("abcdefgh")
    trie.remove("abcdefgh")
    assert _node_count(trie)==1  # only the root remains
    assert len(trie)==0 and list(trie)==[]


def test_remove_keeps_shared_prefix_and_longer_words():
    trie=Trie()
    for w in ["car","card","care","cat"]:
        trie.insert(w)
    trie.remove("card")
    assert list(trie)==["car","care","cat"]
    assert trie.starts_with("car")
    trie.remove("car")  # "car" is a prefix of "care": node must stay
    assert list(trie)==["care","cat"]
    assert trie.search("care")
    trie.remove("care")
    trie.remove("cat")
    assert _node_count(trie)==1


def test_remove_is_a_noop_on_failure():
    trie=Trie()
    trie.insert("cart")
    for bad in ["car","carts","dog",""]:
        with pytest.raises(ValueNotFoundError):
            trie.remove(bad)
    assert list(trie)==["cart"]
    assert len(trie)==1


def test_empty_string_word_roundtrip():
    trie=Trie()
    trie.insert("")
    assert "" in trie and len(trie)==1
    trie.remove("")
    assert "" not in trie and len(trie)==0


def test_random_insert_remove_matches_set_and_stays_minimal():
    import random
    rng=random.Random(4)
    trie,model=Trie(),set()
    for _ in range(400):
        w="".join(rng.choice("abc") for _ in range(rng.randint(0,5)))
        if rng.random()<0.5:
            trie.insert(w)
            model.add(w)
        elif w in model:
            trie.remove(w)
            model.remove(w)
        assert list(trie)==sorted(model)
    for w in list(model):
        trie.remove(w)
    assert _node_count(trie)==1