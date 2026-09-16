from langchain.tools import tool
from app.services.IncidentService import get_incident
from app.services.ServiceService import get_service_status
from app.services.DeploymentService import get_recent_deployments
from app.services.LogService import search_logs
from app.services.MetricsService import get_metrics
from app.services.RunbookService import search_runbooks

@tool
def get_incident_tool(incident_id : str) -> dict:
    """
    Get details about a production incident.

    Args:
        incident_id : The unique ID of the incident.
    """

    return get_incident(incident_id)

@tool
def get_service_status_tool(service_id : str) -> str:
    """
    Get the current status of the service.

    Args:
        service_id : The unique ID of the service.
    """

    return get_service_status(service_id)

@tool
def get_recent_deployments_tool(service_id : str, limit : int = 5) -> list[dict]:
    """
    Get the recent deployments for a service.

    Args:
        service_id : The unique ID of the service.
        limit : maximum limit of deployments
    """

    return get_recent_deployments(service_id, limit)

@tool
def search_logs_tool(service_id : str, query : str, limit : int = 20) -> list[dict]:
    """
    Search logs for a service.
    
    Args:
        service_id : The unique ID of the service.
        query : query related to incident.
        limit : maximum limit of logs.
    """

    return search_logs(service_id,query,limit)

@tool
def search_runbooks_tool(service_id : str, query : str, limit : int = 5) -> list[dict]:
    """
    Search runbooks for a service.
    Args:
        service_id : The unique ID of the service.
        query : query related to incident.
        limit : maximum limit of runbooks.
    """

    return search_runbooks(service_id,query,limit)

@tool
def get_metrics_tool(service_id : str, metric_name : str , limit : int = 20) -> list[dict]:
    """
    Get metrics for a service.
    Args:
        service_id : The unique ID of the service.
        metric_name: name of the metric.
        limit: maximum limit of metrics.
    """
    return get_metrics(service_id,metric_name,limit)