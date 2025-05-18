from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
import os

def train_model_pipeline():
    x = np.array([[10.0], [200.0], [1500.0], [3000.0], [50.0]])
    y = np.array([0, 0, 1, 1, 0])

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x, y)

    output_dir = os.path.join("app", "model")
    os.makedirs(output_dir, exist_ok=True)
    #joblib.dump(model, os.path.join(output_dir, "model.pkl"))
    # Dentro de app/utils/train_model.py
    joblib.dump(model, "model/model.pkl")  # esto es relativo al contenedor


    print("✅ Modelo entrenado y guardado correctamente.")
