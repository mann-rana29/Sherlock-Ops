def get_field(record, field):
    if isinstance(record, dict):
        return record.get(field)

    return getattr(record, field, None)

def validate_evidence(records, service_id, source, limit):
    if not isinstance(records, list):
        raise ValueError(f"Invalid {source} data.")

    if len(records) > limit:
        records = records[:limit]

    for record in records:

        record_service = get_field(record, "service_id")

        if record_service != service_id:
            raise ValueError(
                f"Unrelated service data detected in {source}."
            )

    return records