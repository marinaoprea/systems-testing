import tree

def test_find():
    tr = tree.Tree()

    tr.add(3)
    tr.add(4)
    tr.add(0)
    tr.add(8)
    tr.add(2)

    assert tr.find(3), "error 3 in tree"
    assert tr.find(3).data == 3, "error 3 in tree"
    assert tr.find(-1) == None, "error -1 not in tree"
