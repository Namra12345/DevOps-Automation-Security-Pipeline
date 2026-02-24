from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Demonstrating environment variable usage - common in DevOps
    env_name = os.getenv("ENV_NAME", "Development")
    return f"Hello! This is a secure {env_name} environment."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)