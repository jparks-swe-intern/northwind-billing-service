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
