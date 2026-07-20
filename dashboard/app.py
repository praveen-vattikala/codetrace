import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from listener.analyzer import (
    load_interactions,
    validation_pass_rate,
    average_response_time,
    common_keywords,
    provider_breakdown,
)

st.set_page_config(page_title="CodeTrace Dashboard", layout="wide")

st.title("CodeTrace: Coding Agent Usage Dashboard")
st.caption("Insights generated from logged interactions with the AI coding agent")

interactions = load_interactions()

if not interactions:
    st.warning("No interactions logged yet. Run some requests through agent/cli.py first.")
    st.stop()

# --- Top-level metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Interactions", len(interactions))
col2.metric("Validation Pass Rate", f"{validation_pass_rate(interactions)}%")
col3.metric("Avg Response Time", f"{average_response_time(interactions)}s")

st.divider()

# --- Provider breakdown ---
st.subheader("Provider Usage")
providers = provider_breakdown(interactions)
provider_df = pd.DataFrame(list(providers.items()), columns=["Provider", "Count"])
st.bar_chart(provider_df.set_index("Provider"))

# --- Common keywords ---
st.subheader("Most Common Request Keywords")
keywords = common_keywords(interactions, top_n=10)
keyword_df = pd.DataFrame(keywords, columns=["Keyword", "Frequency"])
st.bar_chart(keyword_df.set_index("Keyword"))

# --- Raw log table ---
st.subheader("All Logged Interactions")
df = pd.DataFrame(interactions)
st.dataframe(df, use_container_width=True)