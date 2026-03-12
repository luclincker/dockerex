from counter import add_one_to_count, remove_one_to_count

def test_add():
    assert add_one_to_count(0) == 1

def test_remove():
    assert remove_one_to_count(1) == 0

def test_remove_no_change():
    assert remove_one_to_count(0) == 0
