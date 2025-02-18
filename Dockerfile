FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn joblib pandas scikit-learn requests
EXPOSE 7500
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7500"]
