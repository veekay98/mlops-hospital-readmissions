import unittest
import requests

class TestFastAPI(unittest.TestCase):
    def test_prediction_endpoint(self):
        response = requests.post(
            "http://localhost:7500/predict/",
            json={"age": 65, "n_medications": 10}
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
