from app.models import Runbook
from app.services.JsonLoaderServce import get_data

def search_runbooks( service_id : str, query : str, limit : int = 5) -> list[Runbook]:
    data = get_data("runbooks")

    if data is None:
        return []

    runbooks = [Runbook.model_validate(r) for r in data]

    runbooks = [r for r in runbooks if r.service_id == service_id]

    limit = min(limit , len(runbooks))

    return runbooks[:limit]
