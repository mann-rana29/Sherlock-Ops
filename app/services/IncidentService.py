from app.models import Incident
import json
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
file_path = f"{BASE_PATH}/utils/sample_data/incidents.json"

def get_incident(incident_id : str) -> Incident:
    with open(file_path, "r" , encoding="utf-8") as file:
        data = json.load(file)

    if data is None:
        return 

    incidents = [Incident.model_validate(incident) for incident in data]

    for incident in incidents:
        if incident.incident_id == incident_id:
            return incident

    raise ValueError("Incident doesn't exist")