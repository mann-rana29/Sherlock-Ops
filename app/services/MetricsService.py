from app.models import MetricSnapshot
from app.services.JsonLoaderServce import get_data

def get_metrics(service_id : str,  metric_name : str, limit: int = 20) -> list[MetricSnapshot]:
    data = get_data("metrics")

    if data is None:
        return []

    metrics = [MetricSnapshot.model_validate(m) for  m in data]

    metrics = [m for m in metrics if m.service_id == service_id and m.metric.value == metric_name]

    limit = min(limit, len(metrics))

    return metrics[:limit]
