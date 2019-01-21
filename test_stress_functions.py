import pytest

from stress_fuctions import get_eq_stress

def test_get_eq_stress():
    assert pytest.approx(get_eq_stress((20,60), state='2d'), 0.1) == 52.9
    #assert get_eq_stress((20,60), state='2d') == 52.9