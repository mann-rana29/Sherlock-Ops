from app.services.JsonLoaderServce import get_data
from app.models import Remediation

def prepare_rollback(incident_id : str , deployment_id : str) -> Remediation:
    pass

def commit_rollback(rollback_id : str, idempotency_key : str) -> Remediation:
    pass
