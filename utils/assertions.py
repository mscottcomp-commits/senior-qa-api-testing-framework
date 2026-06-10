from jsonschema import validate


def assert_status_code(response, expected_status_code):
    """
    Validates that the API returned the expected HTTP status code.
    """
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, "
        f"but got {response.status_code}. Response: {response.text}"
    )


def assert_json_field_exists(response_json, field_name):
    """
    Validates that a specific field exists in the JSON response.
    """
    assert field_name in response_json, f"Expected field '{field_name}' was not found."


def assert_json_field_value(response_json, field_name, expected_value):
    """
    Validates that a specific JSON field has the expected value.
    """
    assert response_json[field_name] == expected_value, (
        f"Expected '{field_name}' to be '{expected_value}', "
        f"but got '{response_json[field_name]}'"
    )


def assert_schema(response_json, schema):
    """
    Validates that the API response matches the expected JSON schema.
    """
    validate(instance=response_json, schema=schema)


def assert_content_type(response, expected_content_type):
    """
    Validates that the API response returns the expected content type.
    Example: application/json
    """
    actual_content_type = response.headers.get("Content-Type", "")

    assert expected_content_type in actual_content_type, (
        f"Expected Content-Type to include '{expected_content_type}', "
        f"but got '{actual_content_type}'"
    )


def assert_response_time_less_than(response, max_seconds):
    """
    Validates that the API response time is below the expected limit.
    """
    actual_seconds = response.elapsed.total_seconds()

    assert actual_seconds < max_seconds, (
        f"Expected response time to be less than {max_seconds} seconds, "
        f"but got {actual_seconds} seconds."
    )