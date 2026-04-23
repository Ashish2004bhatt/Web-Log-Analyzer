import pandas as pd

def sessionize(df: pd.DataFrame, timeout_minutes=30):
    df = df.sort_values(["ip", "timestamp"]).copy()

    df["prev_time"] = df.groupby("ip")["timestamp"].shift(1)

    df["time_diff"] = (df["timestamp"] - df["prev_time"]).dt.total_seconds().fillna(999999)

    df["new_session"] = df["time_diff"] > timeout_minutes * 60

    df["session_id"] = df.groupby("ip")["new_session"].cumsum()

    return df
