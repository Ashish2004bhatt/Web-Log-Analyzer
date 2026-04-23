import pandas as pd
from .cleaner import clean_dataframe
from .feature_engineering import (
    add_time_features,
    add_url_features,
    add_agent_features,
    add_ip_features
)
from .sessionizer import sessionize
import os

def run_step2(input_file, output_file):
    print(f"[+] Loading Step 1 output: {input_file}")
    df = pd.read_parquet(input_file)

    print(f"[+] Loaded {len(df)} rows")

    print("[+] Cleaning data...")
    df = clean_dataframe(df)

    print("[+] Adding time features...")
    df = add_time_features(df)

    print("[+] Adding URL features...")
    df = add_url_features(df)

    print("[+] Adding agent features...")
    df = add_agent_features(df)

    print("[+] Adding IP features...")
    df = add_ip_features(df)

    print("[+] Sessionizing user traffic...")
    df = sessionize(df)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_parquet(output_file, index=False)

    print(f"[✓] Step 2 completed successfully!")
    print(f"[✓] Saved features to {output_file}")


if __name__ == "__main__":
    run_step2(
        input_file="data/processed/apache.parquet",
        output_file="data/features/apache_features.parquet"
    )
