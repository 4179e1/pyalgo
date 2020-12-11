from nqueen import nqueen

def test_nqueen():
    cases = {
        1: 1,
        2: 0,
        3: 0,
        4: 2,
        8: 92,
    }

    for n, want in cases.items():
        cbs = nqueen(n)
        got = len(cbs)
        assert got == want