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

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="MatchPulse",
    page_icon="⚽",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("⚽ MatchPulse")
st.subheader(
    "AI-Powered Match Intelligence Platform for Football Analytics"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

stats = get_match_stats("data/sample_match.json")

with open("data/sample_match.json", "r") as f:
    events = json.load(f)

# --------------------------------------------------
# TOP METRICS
# --------------------------------------------------

st.header("📊 Match Intelligence")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Possession", f"{stats['possession']}%")

with col2:
    st.metric("Pass Accuracy", f"{stats['pass_accuracy']}%")

with col3:
    st.metric("Goals", stats["goals"])

with col4:
    st.metric("Shots", stats["shots"])

with col5:
    st.metric("Pressure", stats["pressure_index"])

# --------------------------------------------------
# LIVE FEED + INSIGHTS
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.header("⚽ Live Match Feed")

    for event in events:

        st.write(
            f"⏱️ {event['minute']}' | "
            f"👤 {event['player']} | "
            f"🎯 {event['event'].upper()}"
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

momentum_data = pd.DataFrame(
    {
        "Minute": [10,20,30,40,50,60,70,80,90],
        "Momentum": [20,35,45,55,70,80,75,90,95]
    }
)

st.line_chart(
    momentum_data.set_index("Minute")
)

# --------------------------------------------------
# LANGUAGE
# --------------------------------------------------

st.header("🌍 Multi-Language Storytelling")

language = st.selectbox(
    "Choose Language",
    ["English", "Telugu", "Hindi"]
)

if language == "English":

    st.success(
        "Blue FC is dominating possession and controlling the rhythm of the game."
    )

elif language == "Telugu":

    st.success(
        "బ్లూ ఎఫ్‌సీ బంతిపై ఆధిపత్యం ప్రదర్శిస్తూ మ్యాచ్‌ను నియంత్రిస్తోంది."
    )

elif language == "Hindi":

    st.success(
        "ब्लू एफसी गेंद पर नियंत्रण रखते हुए मैच की गति तय कर रही है।"
    )

# --------------------------------------------------
# PERSONALIZATION
# --------------------------------------------------

st.header("👤 Personalized Fan Experience")

view = st.radio(
    "Select Mode",
    ["Analyst", "Fan", "Player"]
)

if view == "Analyst":

    st.code(
        analyst_view(stats)
    )

elif view == "Fan":

    st.success(
        fan_view()
    )

else:

    st.info(
        player_view()
    )

# --------------------------------------------------
# RECAP
# --------------------------------------------------

st.header("📝 Automated Match Recap")

st.warning(
    generate_recap()
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "MatchPulse | Synthetic Match Insights Engine | Microsoft Premier League Hackathon"
)
