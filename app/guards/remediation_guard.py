from datetime import datetime, timezone

SUCCESSFUL_STATUSES = {
    "success",
    "successful",
    "succeeded",
    "superseded"
}

def validate_rollback(
    faulty_deployment : dict,
    target_deployment : dict,
    incident : dict
) -> tuple[bool,str]:

    service_id = incident["service_id"]

    if faulty_deployment["service_id"] != service_id:
        return False, "Faulty deployment belongs to another service."

    if target_deployment["service_id"] != service_id:
        return False, "Rollback target belongs to another service."

    if faulty_deployment["deployment_id"] == target_deployment["deployment_id"]:
        return False, "Cannot roll back to the same deployment."

    faulty_time = datetime.fromisoformat(
        faulty_deployment["deployed_at"].replace("Z", "+00:00")
    )

    target_time = datetime.fromisoformat(
        target_deployment["deployed_at"].replace("Z", "+00:00")
    )

    if target_time >= faulty_time:
        return False, "Rollback target must be older than faulty deployment."

    if target_deployment["status"].lower() not in {
        "active", "failed", "unhealthy"
    }:
        return False, "Faulty deployment is not in an eligible state."


    return True, "Rollback validation passed."