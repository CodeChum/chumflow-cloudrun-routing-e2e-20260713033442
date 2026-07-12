from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def health():
    return jsonify(service="chum-flow-test-service", release="hotfix-prod"), 200
