import pandas as pd

def clean_dataframe(df: pd.DataFrame):
    """
    Basic cleaning:
    - drop rows with missing essential fields
    - remove invalid statuses
    - convert data types
    """
    df = df.copy()

    # Remove rows without a URL or timestamp
    df = df.dropna(subset=["url", "timestamp"])

    # Fix sizes
    df["size"] = pd.to_numeric(df["size"], errors="coerce").fillna(0).astype(int)

    # Fix status codes
    df["status"] = pd.to_numeric(df["status"], errors="coerce").astype("Int64")

    return df
