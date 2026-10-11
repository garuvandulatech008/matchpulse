import streamlit as st
import json

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
    layout="wide"
)

st.title("⚽ MatchPulse")
st.subheader("AI Powered Match Intelligence Engine")

stats = get_match_stats("data/sample_match.json")

with open("data/sample_match.json", "r") as f:
    events = json.load(f)

col1, col2 = st.columns(2)

with col1:

    st.header("⚽ Live Match Feed")

    for event in events:

        st.write(
            f"{event['minute']}' | "
            f"{event['player']} | "
            f"{event['event'].upper()}"
        )

with col2:

    st.header("📊 Match Intelligence")

    st.metric(
        "Possession",
        f"{stats['possession']}%"
    )

    st.metric(
        "Pass Accuracy",
        f"{stats['pass_accuracy']}%"
    )

    st.metric(
        "Goals",
        stats["goals"]
    )

    st.metric(
        "Shots",
        stats["shots"]
    )

    st.metric(
        "Pressure Index",
        stats["pressure_index"]
    )

st.header("🧠 AI Narrative")

st.success(
    generate_narrative(stats)
)

st.header("❓ Why It Matters")

st.info(
    explain_moment()
)

language = st.selectbox(
    "🌍 Language",
    ["English", "Telugu", "Hindi"]
)

if language == "Telugu":

    st.success(
        "బ్లూ ఎఫ్‌సీ మ్యాచ్‌పై ఆధిపత్యం చెలాయిస్తోంది."
    )

elif language == "Hindi":

    st.success(
        "ब्लू एफसी मैच पर नियंत्रण बना रही है।"
    )

view = st.radio(
    "Select User Mode",
    ["Analyst", "Fan", "Player"]
)

if view == "Analyst":

    st.write(
        analyst_view(stats)
    )

elif view == "Player":

    st.write(
        player_view()
    )

else:

    st.write(
        fan_view()
    )

st.header("📝 Match Recap")

st.warning(
    generate_recap()
)