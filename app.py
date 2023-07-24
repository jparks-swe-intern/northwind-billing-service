import yaml
from flask import Flask

app = Flask(__name__)

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=8080)

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/invoices")
def list_invoices():
    return {"invoices": []}

@app.errorhandler(404)
def not_found(e):
    return {"error": "not found"}, 404
