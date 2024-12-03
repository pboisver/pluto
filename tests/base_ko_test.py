from pluto import HangnailDiagnoser


def test_hangnail_severe():
    assert HangnailDiagnoser.hangnail(10, 6) == True


def test_hangnail_mild():
    assert HangnailDiagnoser.hangnail(5, 4) == False


def test_hangnail_edge_case():
    assert HangnailDiagnoser.hangnail(10, 5) is True
    

