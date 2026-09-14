from app.models import Service
from app.services.JsonLoaderServce import get_data

def get_service(service_id : str) -> Service:
    data = get_data("services")
    if data is None:
        return 
    
    services = [Service.model_validate(service) for service in data]
    
    for service in services:
        if service.service_id == service_id:
             return service
        
    raise ValueError("Service doesn't exist")

def get_service_status(service_id : str) -> str:
    data = get_data("services")

    if data is None:
        return ""

    services = [Service.model_validate(service)  for service in data]

    for service in services:
        if service.service_id == service_id:
            return service.status

    raise ValueError("Service doesn't exist")