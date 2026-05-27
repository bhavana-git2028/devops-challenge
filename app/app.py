from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

@app.route("/")
def home():
    try:
        r = redis.Redis(host=redis_host, port=6379)
        r.ping()
        return {
            "status": "ok",
            "redis": "connected"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

