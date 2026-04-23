import pandas as pd
from urllib.parse import urlparse

def add_time_features(df: pd.DataFrame):
    df["hour"] = df["timestamp"].dt.hour
    df["minute"] = df["timestamp"].dt.minute
    df["day"] = df["timestamp"].dt.day
    df["weekday"] = df["timestamp"].dt.weekday
    df["is_weekend"] = df["weekday"] >= 5
    return df

def add_url_features(df: pd.DataFrame):
    paths = df["url"].astype(str).apply(urlparse)
    
    df["path"] = paths.apply(lambda x: x.path)
    df["path_length"] = df["path"].apply(len)
    df["path_depth"] = df["path"].apply(lambda p: p.count("/"))

    df["query"] = paths.apply(lambda x: x.query)
    df["query_params"] = df["query"].apply(lambda q: q.count("&") + 1 if q else 0)

    file_ext = df["path"].apply(lambda p: p.split(".")[-1] if "." in p else "")
    df["file_type"] = file_ext

    return df

def add_agent_features(df: pd.DataFrame):
    # VERY simple bot detection
    df["is_bot"] = df["agent"].str.contains(
        "bot|crawl|spider|curl|wget|python",
        case=False,
        regex=True,
        na=False
    )
    return df

def add_ip_features(df: pd.DataFrame):
    # Placeholder for future GeoIP
    df["ip_numeric"] = df["ip"].apply(lambda ip: sum(int(x) << (8*i) for i,x in enumerate(ip.split(".")[::-1])) if ip and "." in ip else 0)
    return df
