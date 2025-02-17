import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow

# Load dataset
df = pd.read_csv("data/cleaned_data.csv")

df.dropna(inplace=True)


X = df.drop("readmitted", axis=1)
y = df["readmitted"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize MLflow
mlflow.set_tracking_uri("http://127.0.0.1:6000")  # Local MLflow tracking

# Train Model
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)

    # Save model
    joblib.dump(model, "model.pkl")
    mlflow.log_artifact("model.pkl")

import optuna

def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 50, 200)
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=10)
print("Best parameters:", study.best_params)
