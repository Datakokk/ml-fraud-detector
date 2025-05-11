# train_model.py

from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
import os

# Example dataset (1 single feature: amount)
X = np.array([[10.0], [200.0], [1500.0], [3000.0], [50.0]])
y = np.array([0, 0, 1, 1, 0])  # 0 = no fraud, 1 = fraud

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model
output_dir = os.path.join("app", "model")
os.makedirs(output_dir, exist_ok=True)
joblib.dump(model, os.path.join(output_dir, "model.pkl"))

print("✅ Modelo entrenado y guardado correctamente.")
