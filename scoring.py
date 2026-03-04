import pandas as pd

def compute_delivery_score(df):
    status_weights = {
        "Kept": 1,
        "In Progress": 0.5,
        "Broken": 0,
        "No Evidence": 0
    }

    df["score"] = df["status"].map(status_weights)

    scores = (
        df.groupby("politician")["score"]
        .mean()
        .reset_index()
        .rename(columns={"score": "delivery_score"})
    )

    return scores
