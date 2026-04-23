# ML Demo Test for Web Log Analyzer
# This file shows a very simple example prediction

from sklearn.ensemble import RandomForestClassifier

# Training dataset (tiny sample)
X = [
    [5, 20, 0],   # Normal
    [10, 30, 1],  # Normal
    [50, 60, 5],  # Suspicious
    [80, 70, 8],  # Suspicious
]

y = [
    0,  # Normal
    0,  # Normal
    1,  # Bot / Suspicious
    1,  # Bot / Suspicious
]

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# ----------------------------------------
# Example test input (change these values)
# ----------------------------------------
ip_requests = 45
avg_url_length = 50
errors_404 = 3

test_input = [[ip_requests, avg_url_length, errors_404]]

prediction = model.predict(test_input)[0]

label = "Suspicious / Bot" if prediction == 1 else "Normal User"

print("\nTest Input Values:")
print(f" - IP Requests: {ip_requests}")
print(f" - Avg URL Length: {avg_url_length}")
print(f" - 404 Errors: {errors_404}")

print("\nPrediction:", label)
