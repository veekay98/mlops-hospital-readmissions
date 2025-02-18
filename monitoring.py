from prometheus_client import start_http_server, Counter
import time

# Define a counter metric
REQUEST_COUNT = Counter("api_requests_total", "Total number of API requests")

def monitor():
    print("✅ Starting Prometheus monitoring on port 7600...")
    start_http_server(7600)  # Prometheus server starts here
    while True:
        REQUEST_COUNT.inc()  # Increment the request count
        print("🔄 Updated request count metric")
        time.sleep(5)  # Sleep to simulate updates every 5 seconds

if __name__ == "__main__":
    monitor()
