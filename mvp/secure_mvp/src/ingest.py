from flask import Flask, request
from pathlib import Path
from datetime import datetime
import uuid

app = Flask(__name__)
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(exist_ok=True)

@app.route("/log", methods=["POST"])
def receive_log():
    data = request.get_data(as_text=True)
    fname = f"log_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex[:8]}.json"
    (LOG_DIR / fname).write_text(data, encoding="utf-8")
    return {"status":"saved","file":fname}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

