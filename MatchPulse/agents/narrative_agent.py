def generate_narrative(stats):

    narrative = f"""
Blue FC is currently controlling the match with
{stats['possession']}% possession and a pass accuracy
of {stats['pass_accuracy']}%.

The team has generated {stats['shots']} shots while
maintaining high attacking pressure.

Momentum is currently favoring Blue FC as they
continue to dominate possession and create
goal-scoring opportunities.
"""

    return narrative
