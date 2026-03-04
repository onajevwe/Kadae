import streamlit as st
import pandas as pd
from scoring import compute_delivery_score

st.title("Kadae – Political Promise Analytics")

df = pd.read_csv("data/sample_promises.csv")
scores = compute_delivery_score(df)

st.subheader("Delivery Scores")
st.dataframe(scores)
