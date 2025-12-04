
def prevod_c_na_f(stupne):
    fahrenheity = stupne * 1.8 + 32
    return fahrenheity


def test_prevod_c_na_f():
    assert prevod_c_na_f(0) == 32
    assert prevod_c_na_f(100) == 212
    