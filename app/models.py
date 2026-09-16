from pydantic import BaseModel
from app.enums import Role, Metric
from datetime import datetime

class Incident(BaseModel):
    incident_id : str
    title : str
    severity : str
    service_id : str
    status : str
    created_at : datetime
    description : str

class Service(BaseModel):
    service_id : str
    name : str
    environment : str
    status : str
    current_deployment_id : str
    team_id : str

class Deployment(BaseModel):
    deployment_id : str
    service_id : str
    version : str
    deployed_at : datetime
    status : str
    commit_sha : str

class LogEvent(BaseModel):
    timestamp : datetime
    service_id : str
    level : str
    message : str

class MetricSnapshot(BaseModel):
    timestamp : datetime
    service_id : str
    metric : Metric
    value : float

class Runbook(BaseModel):
    runbook_id : str
    service_id : str
    title : str
    content : str

class Remediation(BaseModel):
    remediation_id : str
    incident_id : str
    action : str
    target : str
    status : str
    created_by : str
    idempotency_key : str
    created_at : str