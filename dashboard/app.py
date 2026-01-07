import os
import time
from dataclasses import dataclass

import requests
import yaml
from flask import Flask, render_template

REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "2.0"))

app = Flask(__name__)


@dataclass
class InstanceStatus:
    name: str
    version: str
    url: str
    status: str
    http_status: str
    latency_ms: int


def load_instances(config_path: str) -> list[dict]:
    with open(config_path, "r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    return config.get("instances", [])


def check_instance(instance: dict) -> InstanceStatus:
    name = instance.get("name", "unknown")
    version = instance.get("version", "unknown")
    url = instance.get("url", "")

    start = time.time()
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        latency_ms = int((time.time() - start) * 1000)
        return InstanceStatus(
            name=name,
            version=version,
            url=url,
            status="UP" if response.ok else "DEGRADED",
            http_status=str(response.status_code),
            latency_ms=latency_ms,
        )
    except requests.RequestException:
        latency_ms = int((time.time() - start) * 1000)
        return InstanceStatus(
            name=name,
            version=version,
            url=url,
            status="DOWN",
            http_status="-",
            latency_ms=latency_ms,
        )


@app.route("/")
def index():
    config_path = os.getenv("DASHBOARD_CONFIG", "/config/instances.yml")
    instances = load_instances(config_path)
    statuses = [check_instance(instance) for instance in instances]
    return render_template("index.html", instances=statuses)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
