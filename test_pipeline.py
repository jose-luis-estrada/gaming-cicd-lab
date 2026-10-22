import pytest
from pipeline import calculate_total_events, validate_events

def test_calculate_total_events():
    events = [10, 20, 15, 5]

    result = calculate_total_events(events)

    assert result == 50

def test_validate_events_valid():
    events = [10, 20, 15]

    result = validate_events(events)

    assert result is True

def test_validate_events_invalid():
    events = [10, -20, 15]

    with pytest.raises(ValueError):
        validate_events(events)