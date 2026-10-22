def calculate_total_events(events):
    return sum(events)


def validate_events(events):
    for event in events:
        if event < 0:
            raise ValueError("Event counts cannot be negative")

    return True


if __name__ == "__main__":
    player_events = [10, 20, 15, 5]
    total = calculate_total_events(player_events)

    print(f"Total events processed: {total}")