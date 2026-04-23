import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from .models_ml import (
    get_random_forest,
    get_xgboost,
    get_isolation_forest,
    save_model
)
from .ml_utils import (
    build_feature_target,
    split_dataset,
    evaluate_model
)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


def save_confusion_matrix(model, X_test, y_test, name):
    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds)

    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Confusion Matrix - {name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    os.makedirs("results/ml", exist_ok=True)
    plt.savefig(f"results/ml/{name}_confusion_matrix.png")
    plt.close()


def save_accuracy_bar(models, accuracies):
    plt.figure(figsize=(6, 4))
    plt.bar(models, accuracies)
    plt.ylim(0.90, 1.0)
    plt.ylabel("Accuracy (decimal)")
    plt.title("Model Accuracy Comparison")

    os.makedirs("results/ml", exist_ok=True)
    plt.savefig("results/ml/accuracy_comparison.png")
    plt.close()


def run_training():
    print("[+] Loading features...")
    df = pd.read_parquet("data/features/apache_features.parquet")
    print(f"[+] Loaded {len(df)} rows")

    print("[+] Preparing dataset ...")
    X, y = build_feature_target(df)
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    accuracies = []
    model_names = []

    # --------------------------
    # Model 1 — Random Forest
    # --------------------------
    print("\n[+] Training RandomForest...")
    rf = get_random_forest()
    rf.fit(X_train, y_train)

    preds_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, preds_rf)

    # Show both formats
    print(f"RandomForest Accuracy (decimal): {acc_rf:.6f}")
    print(f"RandomForest Accuracy (%): {acc_rf * 100:.2f}%")

    accuracies.append(acc_rf)
    model_names.append("RandomForest")

    print(classification_report(y_test, preds_rf))
    save_model(rf, "models/ml/random_forest.pkl")
    save_confusion_matrix(rf, X_test, y_test, "RandomForest")
    print("[✓] Saved RF model & confusion matrix")

    # --------------------------
    # Model 2 — XGBoost
    # --------------------------
    print("\n[+] Training XGBoost...")
    xgb = get_xgboost()
    xgb.fit(X_train, y_train)

    preds_xgb = xgb.predict(X_test)
    acc_xgb = accuracy_score(y_test, preds_xgb)

    # Show both formats
    print(f"XGBoost Accuracy (decimal): {acc_xgb:.6f}")
    print(f"XGBoost Accuracy (%): {acc_xgb * 100:.2f}%")

    accuracies.append(acc_xgb)
    model_names.append("XGBoost")

    print(classification_report(y_test, preds_xgb))
    save_model(xgb, "models/ml/xgboost.pkl")
    save_confusion_matrix(xgb, X_test, y_test, "XGBoost")
    print("[✓] Saved XGBoost model & confusion matrix")

    # --------------------------
    # Model 3 — Isolation Forest
    # --------------------------
    print("\n[+] Training IsolationForest...")
    iso = get_isolation_forest()
    iso.fit(X_train)
    save_model(iso, "models/ml/iso_forest.pkl")
    print("[✓] Saved IsolationForest model")

    # --------------------------
    # Save Accuracy Bar Graph
    # --------------------------
    save_accuracy_bar(model_names, accuracies)
    print("[✓] Saved Accuracy Comparison Graph")

    print("\n[✓] Step 3 ML Training Completed with Graphs!")


if __name__ == "__main__":
    run_training()
