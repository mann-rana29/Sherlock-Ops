import pytest

from app.guards.input_guard import validate_incident, validate_incident_id

#Incident ID tests
def test_valid_incident_id():
    result = validate_incident_id("INC-1042")

    assert result == "INC-1042"

def test_incident_id_with_spaces():
    result = validate_incident_id(" INC-1042 ")

    assert result == "INC-1042"

def test_invalid_incident_id():
    with pytest.raises(ValueError):
        validate_incident_id("INVALID-1042")

def test_incident_id_must_be_string():
    with pytest.raises(ValueError):
        validate_incident_id(1042)


#Incident record tests

def test_valid_incident():
    incident = {
        "incident_id" : "INC-1042",
        "service_id" : "svc-payments"
    }

    result = validate_incident(incident)

    assert result is True

def test_missing_incident():
    with pytest.raises(ValueError):
        validate_incident(None)

def test_incident_missing_service_id():
    incident = {
        "incident_id" : "INC-1042" 
    }

    with pytest.raises(ValueError):
        validate_incident(incident)