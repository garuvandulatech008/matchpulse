def analyst_view(stats):

    return f"""
Possession: {stats['possession']}%

Pass Accuracy: {stats['pass_accuracy']}%

Goals: {stats['goals']}

Shots: {stats['shots']}

Pressure Index: {stats['pressure_index']}
"""


def fan_view():

    return """
Blue FC is dominating the match with
aggressive attacking football and better
control of possession.
"""


def player_view():

    return """
Player Focus: Alex

Goals: 1

Shots: 2

Key Contribution:
Scored the opening goal and led several
attacking movements.
"""