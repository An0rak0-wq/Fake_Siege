import pytest
from Games import *

defenmloc = {
    "Surge": "r1",
    "Vortex": "r2"
}

atkenmloc = {
    "Citadel": "r1",
    "Bulwark": "r2"
}

def test_enmcheck_occupied(): 
    expected_output = (True, "Citadel")
    result = enmcheck("r1", atkenmloc)
    assert result == expected_output, f"Expected {expected_output}, but got {result}" 

def test_enmcheck_empty():
    expected_output = (False, "")
    result = enmcheck("r3", atkenmloc)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"