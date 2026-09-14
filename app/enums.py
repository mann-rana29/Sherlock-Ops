from enum import Enum

class Role(Enum):
    engineer = "engineer"
    senior_engineer = "senior_engineer"
    incident_commander = "incident_commander"
    admin = "admin"

class Metric(Enum):
    error_rate = "error_rate"
    latency_ms = "latency_ms"
    request_count = "request_count"