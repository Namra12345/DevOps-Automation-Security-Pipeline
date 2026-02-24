from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    env_name = os.getenv("ENV_NAME", "Development")
    return f"Hello! This is a secure {env_name} environment."

if __name__ == "__main__":
    # Get host from environment variable, default to '127.0.0.1' for safety
    # In Docker, we will pass '0.0.0.0' as an ENV variable later if needed
    host_ip = os.getenv("APP_HOST", "127.0.0.1") 
    app.run(host=host_ip, port=5000)