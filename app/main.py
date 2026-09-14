from app.services.IncidentService import get_incident
from app.services.ServiceService import get_service, get_service_status
from app.services.LogService import search_logs

print(search_logs("svc-search", "Database connection",0))