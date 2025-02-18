import unittest
import requests

class TestFastAPI(unittest.TestCase):


    def test_prediction_endpoint():
        url = "http://127.0.0.1:7500/predict"
        payload = {
                      "age": 45,
                      "time_in_hospital": 5,
                      "n_lab_procedures": 30,
                      "n_procedures": 2,
                      "n_medications": 10,
                      "n_outpatient": 1,
                      "n_inpatient": 0,
                      "n_emergency": 0,
                      "medical_specialty": "Endocrinology",
                      "diag_1": "250.02",
                      "diag_2": "401.1",
                      "diag_3": "E11.9",
                      "glucose_test": 140,
                      "A1Ctest": 6.5,
                      "change": "Yes",
                      "diabetes_med": "Metformin"
                    }  # Make sure this matches your expected input format

        response = requests.post(url, json=payload)

        print("Response Status Code:", response.status_code)
        print("Response Body:", response.text)  # Print error details

        assert response.status_code == 200, f"API Error: {response.text}"

if __name__ == "__main__":
    unittest.main()
