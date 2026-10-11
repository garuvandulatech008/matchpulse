import streamlit as st
import json
import pandas as pd

from agents.stats_agent import get_match_stats
from agents.narrative_agent import generate_narrative
from agents.explainability_agent import explain_moment
from agents.personalization_agent import (
    analyst_view,
    fan_view,
    player_view
)
from agents.recap_agent import generate_recap

st.set_page_config(
    page_title="MatchPulse",
    page_icon="⚽",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("⚽ MatchPulse")
st.markdown(
    "### AI-Powered Football Intelligence Platform"
)

stats = get_match_stats(
    "data/sample_match.json"
)

with open(
    "data/sample_match.json",
    "r"
) as f:

    events = json.load(f)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.header("📊 Match Intelligence")

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric(
    "Possession",
    f"{stats['possession']}%"
)

k2.metric(
    "Pass Accuracy",
    f"{stats['pass_accuracy']}%"
)

k3.metric(
    "Goals",
    stats["goals"]
)

k4.metric(
    "Shots",
    stats["shots"]
)

k5.metric(
    "Pressure",
    stats["pressure_index"]
)

# --------------------------------------------------
# LIVE FEED + INSIGHTS
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.header("⚽ Live Match Feed")

    for event in events:

        st.write(
            f"{event['minute']}' | "
            f"{event['player']} | "
            f"{event['event'].upper()}"
        )

with right:

    st.header("🧠 AI Narrative")

    st.success(
        generate_narrative(stats)
    )

    st.header("❓ Why It Matters")

    st.info(
        explain_moment()
    )

# --------------------------------------------------
# MOMENTUM CHART
# --------------------------------------------------

st.header("📈 Match Momentum")

momentum_data = pd.DataFrame({
    "Minute": [10,20,30,40,50,60,70,80,90],
    "Momentum": [20,35,50,60,70,80,78,90,95]
})

st.line_chart(
    momentum_data.set_index(
        "Minute"
    )
)

# --------------------------------------------------
# PERSONALIZATION
# --------------------------------------------------

st.header("👤 Personalized Experience")

user_mode = st.radio(
    "Select View Mode",
    ["Analyst", "Fan", "Player"]
)

if user_mode == "Analyst":

    st.code(
        analyst_view(stats)
    )

elif user_mode == "Player":

    st.info(
        player_view()
    )

else:

    st.success(
        fan_view()
    )

# --------------------------------------------------
# MULTI LANGUAGE
# --------------------------------------------------

st.header("🌍 Multi-Language Storytelling")

language = st.selectbox(
    "Select Language",
    [
        "English",
        "Telugu",
        "Hindi"
    ]
)

if language == "English":

    st.write(
        "Blue FC is dominating possession and controlling the rhythm of the game."
    )

elif language == "Telugu":

    st.write(
        "బ్లూ ఎఫ్‌సీ మ్యాచ్‌పై ఆధిపత్యం చెలాయిస్తోంది."
    )

else:

    st.write(
        "ब्लू एफसी मैच पर नियंत्रण बनाए हुए है।"
    )

# --------------------------------------------------
# MATCH RECAP
# --------------------------------------------------

st.header("📝 Automated Match Recap")

st.warning(
    generate_recap()
)

# --------------------------------------------------
# AGENT ARCHITECTURE
# --------------------------------------------------

st.header("🤖 Multi-Agent Workflow")

st.markdown("""
Event Agent  
⬇️  
Stats Agent  
⬇️  
Narrative Agent  
⬇️  
Explainability Agent  
⬇️  
Personalization Agent  
⬇️  
Recap Agent
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "MatchPulse | Microsoft Premier League Hackathon Submission"
)
