def calculate_total_events(events):
    return max(events)


if __name__ == "__main__":
    player_events = [10, 20, 15, 5]
    total = calculate_total_events(player_events)

    print(f"Total events processed: {total}")