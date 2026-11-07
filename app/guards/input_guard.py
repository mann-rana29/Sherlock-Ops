import re

def validate_incident_id(incident_id : str):
    if not isinstance(incident_id, str):
        raise ValueError("Incident ID must be a string.")

    if not re.fullmatch(r"INC-\d{4,}", incident_id.strip()):
        raise ValueError("Invalid incident ID format.")

    return incident_id.strip()

def validate_incident(incident):
    if incident is None:
        raise ValueError("Incident does not exist.")

    incident_id = (
        incident.get("incident_id")
        if isinstance(incident,dict)
        else getattr(incident, "incident_id", None)
    )

    service_id = (
        incident.get("service_id")
        if isinstance(incident,dict)
        else getattr(incident, "service_id", None)
    )

    if not incident_id or not service_id:
        raise ValueError("Incident is missing required information.")

    if not incident_id.startswith("INC-"):
        raise ValueError("Invalid incident record.")

    return True