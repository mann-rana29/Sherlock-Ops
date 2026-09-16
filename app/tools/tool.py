from langchain.tools import tool
from app.services.IncidentService import get_incident

@tool
def get_incident(incident_id : str) -> dict:
    """
    Get details about a production incident.

    Args:
        incident_id : The unique ID of the incident.
    """

    return get_incident()

