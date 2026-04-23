import tensorflow as tf
from tensorflow.keras import layers, models

# ------------------------------
# LSTM Model for Traffic Forecasting
# ------------------------------
def build_lstm_model(input_shape):
    model = models.Sequential([
        layers.LSTM(64, return_sequences=True, input_shape=input_shape),
        layers.LSTM(32),
        layers.Dense(16, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(loss="mse", optimizer="adam")
    return model


# ------------------------------
# CNN Model for Log Classification
# ------------------------------
def build_cnn_model(input_shape, num_classes=2):
    model = models.Sequential([
        layers.Conv1D(64, 3, activation='relu', input_shape=input_shape),
        layers.MaxPooling1D(2),
        layers.Conv1D(128, 3, activation='relu'),
        layers.GlobalMaxPooling1D(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model
