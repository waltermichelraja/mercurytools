import pytest
from mercurytools.graph import Graph
from mercurytools.core.exceptions import ValueNotFoundError


def test_add_vertex_and_edge():
    g=Graph()
    g.add_edge("a","b")
    assert "a" in g and "b" in g
    assert g.has_edge("a","b")
    assert g.has_edge("b","a")  # undirected by default


def test_directed_edge_is_one_way():
    g=Graph(directed=True)
    g.add_edge("a","b")
    assert g.has_edge("a","b")
    assert not g.has_edge("b","a")


def test_add_vertex_noop_on_duplicate():
    g=Graph()
    g.add_vertex("a")
    g.add_vertex("a")
    assert len(g)==1


def test_weighted_edge():
    g=Graph()
    g.add_edge("a","b",weight=5)
    assert g.weight("a","b")==5
    assert g.weight("b","a")==5


def test_unweighted_edge_weight_is_none():
    g=Graph()
    g.add_edge("a","b")
    assert g.weight("a","b") is None


def test_weight_missing_edge_raises():
    g=Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    with pytest.raises(ValueNotFoundError):
        g.weight("a","b")


def test_edge_count_undirected():
    g=Graph()
    g.add_edge("a","b")
    g.add_edge("b","c")
    assert g.edge_count==2
    g.add_edge("a","b")  # re-adding shouldn't double count
    assert g.edge_count==2


def test_edge_count_directed():
    g=Graph(directed=True)
    g.add_edge("a","b")
    g.add_edge("b","a")
    assert g.edge_count==2  # two distinct directed edges


def test_neighbors():
    g=Graph()
    g.add_edge("a","b")
    g.add_edge("a","c")
    assert set(g.neighbors("a"))=={"b","c"}


def test_neighbors_missing_vertex_raises():
    g=Graph()
    with pytest.raises(ValueNotFoundError):
        list(g.neighbors("missing"))


def test_degree():
    g=Graph()
    g.add_edge("a","b")
    g.add_edge("a","c")
    assert g.degree("a")==2
    assert g.degree("b")==1


def test_degree_missing_vertex_raises():
    g=Graph()
    with pytest.raises(ValueNotFoundError):
        g.degree("missing")


def test_remove_edge():
    g=Graph()
    g.add_edge("a","b")
    g.remove_edge("a","b")
    assert not g.has_edge("a","b")
    assert not g.has_edge("b","a")
    assert g.edge_count==0


def test_remove_edge_missing_raises():
    g=Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    with pytest.raises(ValueNotFoundError):
        g.remove_edge("a","b")


def test_remove_vertex():
    g=Graph()
    g.add_edge("a","b")
    g.add_edge("a","c")
    g.add_edge("b","c")
    g.remove_vertex("a")
    assert "a" not in g
    assert not g.has_edge("b","a")
    assert g.has_edge("b","c")
    assert g.edge_count==1


def test_remove_vertex_missing_raises():
    g=Graph()
    with pytest.raises(ValueNotFoundError):
        g.remove_vertex("missing")


def test_remove_vertex_directed():
    g=Graph(directed=True)
    g.add_edge("a","b")
    g.add_edge("c","a")
    g.add_edge("a","d")
    assert g.edge_count==3
    g.remove_vertex("a")
    assert "a" not in g
    assert not g.has_edge("c","a")
    assert g.edge_count==0


def test_bfs_visits_reachable_once():
    g=Graph()
    g.add_edge("a","b")
    g.add_edge("a","c")
    g.add_edge("b","d")
    g.add_edge("c","d")
    result=list(g.bfs("a"))
    assert result[0]=="a"
    assert set(result)=={"a","b","c","d"}
    assert len(result)==len(set(result))


def test_bfs_does_not_visit_unreachable():
    g=Graph(directed=True)
    g.add_edge("a","b")
    g.add_vertex("isolated")
    result=list(g.bfs("a"))
    assert "isolated" not in result


def test_bfs_missing_start_raises():
    g=Graph()
    with pytest.raises(ValueNotFoundError):
        list(g.bfs("missing"))


def test_dfs_visits_reachable_once():
    g=Graph()
    g.add_edge("a","b")
    g.add_edge("a","c")
    g.add_edge("b","d")
    g.add_edge("c","d")
    result=list(g.dfs("a"))
    assert result[0]=="a"
    assert set(result)=={"a","b","c","d"}
    assert len(result)==len(set(result))


def test_dfs_missing_start_raises():
    g=Graph()
    with pytest.raises(ValueNotFoundError):
        list(g.dfs("missing"))


def test_bfs_dfs_agree_on_reachable_set():
    g=Graph(directed=True)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_vertex(99)  # unreachable
    assert set(g.bfs(1))==set(g.dfs(1))==({1,2,3,4,5})


def test_clear():
    g=Graph()
    g.add_edge("a","b")
    g.clear()
    assert len(g)==0
    assert g.edge_count==0


def test_len_and_iter():
    g=Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    assert len(g)==2
    assert set(g)=={"a","b"}


def test_repr():
    g=Graph()
    g.add_vertex("a")
    r=repr(g)
    assert "undirected" in r and "a" in r