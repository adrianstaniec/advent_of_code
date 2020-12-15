import sol


def test_sol_036():
    assert sol.main([0, 3, 6]) == 436

def test_sol_132():
    assert sol.main([1, 3, 2]) == 1


def test_sol_213():
    assert sol.main([2, 1, 3]) == 10


def test_sol_123():
    assert sol.main([1, 2, 3]) == 27


def test_sol_231():
    assert sol.main([2, 3, 1]) == 78


def test_sol_321():
    assert sol.main([3, 2, 1]) == 438


def test_sol_312():
    assert sol.main([3, 1, 2]) == 1836
