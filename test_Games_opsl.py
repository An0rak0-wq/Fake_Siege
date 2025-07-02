import pytest
from Games import *

def test_opsl_atk1(monkeypatch):
    mock_inputs = iter(["1"])

    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    expected_output = ("180", "AR", "Handgun", "Increased Speed")
    result = opsl("atk")
    assert result == expected_output, f"Expected {expected_output}, but got {result}" 

def test_opsl_atk2(monkeypatch):
    mock_inputs = iter(["2"])

    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    expected_output = ("160", "SMG", "Claws", "Adrenaline Boost")
    result = opsl("atk")
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_opsl_def1(monkeypatch):
    mock_inputs = iter(["1"])

    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    expected_output = ("150", "Shotgun", "Handgun", "Fortify Wall")
    result = opsl("def")
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_opsl_def2(monkeypatch):
    mock_inputs = iter(["2"])

    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    expected_output = ("170", "LMG", "Handgun", "Deployable Shield")
    result = opsl("def")
    assert result == expected_output, f"Expected {expected_output}, but got {result}"