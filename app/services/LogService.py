from app.models import LogEvent
from app.services.JsonLoaderServce import get_data

def search_logs(service_id : str, query: str, limit: int = 20) -> list[LogEvent]:
    data = get_data("logs")

    if data is None:
        return []

    logs =  [LogEvent.model_validate(log) for log in data]

    logs = [log for log in logs if log.service_id == service_id]

    limit = min(limit, len(logs))
    
    return logs[:limit]