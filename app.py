from flask import Flask
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    return {
        "message": "Flask Environment Config App",
        "environment": app.config["APP_ENV"],
        "debug": app.config["DEBUG"]
    }


@app.route("/db-test")
def db_test():
    try:
        conn = psycopg2.connect(
            host=app.config["DB_HOST"],
            port=app.config["DB_PORT"],
            dbname=app.config["DB_NAME"],
            user=app.config["DB_USER"],
            password=app.config["DB_PASSWORD"]
        )

        conn.close()
        return {"database": "connected successfully"}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
