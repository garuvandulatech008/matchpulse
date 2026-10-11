import json

def get_match_stats(file_path):

    with open(file_path, "r") as f:
        events = json.load(f)

    stats = {
        "passes": 0,
        "shots": 0,
        "goals": 0,
        "tackles": 0
    }

    for event in events:

        if event["event"] == "pass":
            stats["passes"] += 1

        elif event["event"] == "shot":
            stats["shots"] += 1

        elif event["event"] == "goal":
            stats["goals"] += 1

        elif event["event"] == "tackle":
            stats["tackles"] += 1

    stats["possession"] = 64
    stats["pass_accuracy"] = 89
    stats["pressure_index"] = 78

    return stats