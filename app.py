from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)


@app.route("/")
def home():
    count = redis_client.incr("hits")
    return f"""
    <h1>Flask Redis Docker Compose App</h1>
    <p>This page has been viewed {count} times.</p>
    <p>This app is running with Flask and Redis using Docker Compose.</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)