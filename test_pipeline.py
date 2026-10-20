from pipeline import calculate_total_events

def test_calculate_total_events():
    events = [10, 20, 15, 5]

    result = calculate_total_events(events)

    assert result == 50