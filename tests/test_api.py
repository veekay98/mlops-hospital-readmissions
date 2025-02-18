import unittest
import requests

class TestFastAPI(unittest.TestCase):


    def test_prediction_endpoint():
        url = "http://127.0.0.1:7500/predict"
        payload = {"some": "data"}  # Make sure this matches your expected input format

        response = requests.post(url, json=payload)

        print("Response Status Code:", response.status_code)
        print("Response Body:", response.text)  # Print error details

        assert response.status_code == 200, f"API Error: {response.text}"

if __name__ == "__main__":
    unittest.main()
