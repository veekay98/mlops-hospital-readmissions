from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")

# Expected columns (ensure this matches `check_features.py` output)
EXPECTED_COLUMNS = ['age', 'time_in_hospital', 'n_lab_procedures', 'n_procedures',
                    'n_medications', 'n_outpatient', 'n_inpatient', 'n_emergency',
                    'medical_specialty', 'diag_1', 'diag_2', 'diag_3',
                    'glucose_test', 'A1Ctest', 'change', 'diabetes_med']

@app.post("/predict/")
def predict(data: dict):
    # Convert input into DataFrame
    df = pd.DataFrame([data])

    # Ensure all expected columns are present
    missing_cols = set(EXPECTED_COLUMNS) - set(df.columns)
    for col in missing_cols:
        df[col] = 0  # Add missing columns with default values

    # Ensure column order matches training
    df = df[EXPECTED_COLUMNS]

    # Make prediction
    prediction = model.predict(df)[0]
    return {"prediction": int(prediction)}
