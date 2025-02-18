import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

# Print feature names the model was trained on
print("Model expects the following features:\n", model.feature_names_in_)
