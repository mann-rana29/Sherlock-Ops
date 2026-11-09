import pytest

from app.guards.evidence_guard import validate_evidence

def test_valid_evidence():
    records = [
        {"service_id" : "svc-payments", "message" : "500 error"},
        {"service_id" : "svc-payments", "message" : "Timeout"}
    ]

    result = validate_evidence(
        records=records,
        service_id="svc-payments",
        source="logs",
        limit=20
    )

    assert len(result) == 2
    assert result == records

def test_empty_evidence():
    result = validate_evidence(
        [],
        service_id="svc-payments",
        source="logs",
        limit=20
    )

    assert result == []

def test_evidence_exceeding_limit():
    records = [
        {"service_id": "svc-payments", "message": f"Error {i}"}
        for i in range(25)
    ]

    result = validate_evidence(
        records,
        service_id="svc-payments",
        source="logs",
        limit=20
    )

    assert len(result) == 20

def test_unrelated_service_evidence():
    records = [
        {"service_id": "svc-payments", "message": "500 error"},
        {"service_id": "svc-search", "message": "Timeout"}
    ]

    with pytest.raises(ValueError):
        validate_evidence(
            records,
            service_id="svc-payments",
            source="logs",
            limit=20
        )

def test_evidence_must_be_a_list():
    records = {
        "service_id" : "svc-payments",
        "message" : "500 error"
    }

    with pytest.raises(ValueError):
        validate_evidence(
            records,
            "svc-payments",
            "logs",
            20
        )

def test_unrelated_service_after_limit_is_still_checked():
    records = [
        {"service_id": "svc-payments", "message": f"Error {i}"}
        for i in range(20)
    ]

    records.append({
        "service_id": "svc-search",
        "message": "Unrelated error"
    })

    with pytest.raises(ValueError):
        validate_evidence(
            records,
            "svc-payments",
            "logs",
            20
        )