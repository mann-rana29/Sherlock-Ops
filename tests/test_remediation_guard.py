import pytest

from app.guards.remediation_guard import validate_rollback

@pytest.fixture
def incident():
    return {
        "incident_id" : "INC-1042",
        "service_id" : "svc-payments"
    }

@pytest.fixture
def faulty_deployment():
    return {
        "deployment_id": "dep-8821",
        "service_id": "svc-payments",
        "version": "2026.09.13.4",
        "deployed_at": "2026-09-13T14:01:00Z",
        "status": "active"
    }

@pytest.fixture
def target_deployment():
    return {
        "deployment_id": "dep-8819",
        "service_id": "svc-payments",
        "version": "2026.09.12.8",
        "deployed_at": "2026-09-12T18:30:00Z",
        "status": "superseded"
    }

def test_valid_rollback(
    faulty_deployment,
    target_deployment,
    incident
):
    valid, message = validate_rollback(
        faulty_deployment,
        target_deployment,
        incident
    )

    assert valid is True
    assert message == "Rollback validation passed."

def test_cannot_rollback_to_same_deployment(
    faulty_deployment,
    incident
):
    valid, message = validate_rollback(
        faulty_deployment,
        faulty_deployment,
        incident
    )

    assert valid is False
    assert message == "Cannot roll back to the same deployment"

def test_target_must_belong_to_same_service(
    faulty_deployment,
    target_deployment,
    incident
):
    target_deployment["service_id"] = "svc-search"

    valid , message = validate_rollback(
        faulty_deployment,
        target_deployment,
        incident
    )

    assert valid is False
    assert message == "Rollback target belongs to another service"

def test_target_must_be_older(
    faulty_deployment,
    target_deployment,
    incident
):
    target_deployment["deployed_at"] = "2026-09-14T10:00:00Z"

    valid, message = validate_rollback(
        faulty_deployment,
        target_deployment,
        incident
    )

    assert valid is False
    assert message == "Rollback target must be older than faulty deployment."


def test_target_must_be_successful(
    faulty_deployment,
    target_deployment,
    incident
):
    target_deployment["status"] = "failed"

    valid, message = validate_rollback(
        faulty_deployment,
        target_deployment,
        incident
    )

    assert valid is False
    assert message == "Rollback target was not previously successful."


def test_faulty_deployment_must_be_eligible(
    faulty_deployment,
    target_deployment,
    incident
):
    faulty_deployment["status"] = "superseded"

    valid, message = validate_rollback(
        faulty_deployment,
        target_deployment,
        incident
    )

    assert valid is False
    assert message == "Faulty deployment is not in an eligible state."


def test_invalid_timestamp(
    faulty_deployment,
    target_deployment,
    incident
):
    target_deployment["deployed_at"] = "invalid-date"

    valid, message = validate_rollback(
        faulty_deployment,
        target_deployment,
        incident
    )

    assert valid is False
    assert message == "Invalid deployment timestamp."