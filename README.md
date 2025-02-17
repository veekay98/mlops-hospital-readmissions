# MLOps Hospital Readmissions 🚀

## Overview
This repository contains an **end-to-end MLOps pipeline** for predicting hospital readmissions.

## Features
- **Data Versioning**: Uses DVC to track dataset changes
- **Experiment Tracking**: Logs models using MLflow
- **CI/CD Pipeline**: Automates model training with GitHub Actions
- **Model Deployment**: Deploys a FastAPI-based prediction service
- **Monitoring**: Tracks API performance with Prometheus

## Quick Start
```bash
git clone https://github.com/veekay98/mlops-hospital-readmissions.git
cd mlops-hospital-readmissions
pip install -r requirements.txt
python train_model.py
uvicorn app:app --host 0.0.0.0 --port 8000
