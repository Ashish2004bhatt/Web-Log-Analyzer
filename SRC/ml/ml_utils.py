import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

def build_feature_target(df):
    X = df[[
        "hour", "weekday", "path_length", "path_depth",
        "query_params", "size", "status", "ip_numeric"
    ]].copy()

    # Target: bot/human detection
    y = df["is_bot"].astype(int)

    return X, y

def split_dataset(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    print("\n=== Evaluation Report ===")
    print(classification_report(y_test, preds))
    print("Accuracy:", accuracy_score(y_test, preds))
