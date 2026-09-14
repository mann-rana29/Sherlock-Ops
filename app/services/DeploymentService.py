import json
from pathlib import Path

from app.models import Deployment

BASE_PATH = Path(__file__).resolve().parent.parent
file_path = f"{BASE_PATH}/utils/sample_data/deployments.json"

def get_recent_deployments(service_id: str | None = None, limit : int =5) -> list[Deployment]:
    with open(file_path, "r" , encoding="utf-8") as file:
        data = json.load(file)

    if data is None:
        return []

    deployments = [Deployment.model_validate(dep) for dep in data]

    if service_id is not None:
        deployments = [deployment for deployment in deployments if deployment.service_id == service_id]

    limit = min(limit, len(deployments))

    return deployments[:limit]

# print(get_recent_deployments("svc-search"))