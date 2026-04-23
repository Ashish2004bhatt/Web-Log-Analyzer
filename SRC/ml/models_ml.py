from sklearn.ensemble import RandomForestClassifier, IsolationForest
from xgboost import XGBClassifier
import joblib


import os

def get_random_forest():
    return RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_split=5,
        n_jobs=-1,
        random_state=42
    )

def get_xgboost():
    return XGBClassifier(
        n_estimators=150,
        max_depth=10,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        tree_method="hist",
        random_state=42
    )

def get_isolation_forest():
    return IsolationForest(
        n_estimators=150,
        contamination=0.01,
        random_state=42
    )

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)
