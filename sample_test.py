import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        pytest.param(1, 1, 2, id="t1"),
        pytest.param(2, 2, 4, id="t2"),
        pytest.param(2, 1, 3, id="t3"),
        pytest.param(2, 3, 5, id="t4"),
        pytest.param(3, 4, 7, id="t5"),
    ],
)
def test_addon(a, b, expected):
    print(f"{a}, {b}, {expected}")
    assert a + b == expected
