import pytest

from config import MAX_RESPONSE_TIME_SECONDS
from utils.api_client import APIClient
from utils.assertions import (
    assert_status_code,
    assert_json_field_exists,
    assert_json_field_value,
    assert_content_type,
    assert_response_time_less_than
)
from data.test_data import CREATE_POST_PAYLOAD, UPDATE_POST_PAYLOAD


@pytest.mark.smoke
@pytest.mark.regression
def test_create_post():
    """
    QA Risk Covered:
    Verifies that a post can be created with valid request data.

    Passing Test Proves:
    The API accepts a valid create-post payload and returns JSON with the created post details within the expected response time.
    """

    response = APIClient.post("/posts", CREATE_POST_PAYLOAD)

    assert_status_code(response, 201)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)

    response_json = response.json()

    assert_json_field_value(response_json, "title", CREATE_POST_PAYLOAD["title"])
    assert_json_field_value(response_json, "body", CREATE_POST_PAYLOAD["body"])
    assert_json_field_value(response_json, "userId", CREATE_POST_PAYLOAD["userId"])
    assert_json_field_exists(response_json, "id")


@pytest.mark.regression
def test_update_post():
    """
    QA Risk Covered:
    Verifies that a post can be updated.

    Passing Test Proves:
    The API accepts update payloads and returns JSON with the updated post information within the expected response time.
    """

    response = APIClient.put("/posts/1", UPDATE_POST_PAYLOAD)

    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)

    response_json = response.json()

    assert_json_field_value(response_json, "id", UPDATE_POST_PAYLOAD["id"])
    assert_json_field_value(response_json, "title", UPDATE_POST_PAYLOAD["title"])
    assert_json_field_value(response_json, "body", UPDATE_POST_PAYLOAD["body"])
    assert_json_field_value(response_json, "userId", UPDATE_POST_PAYLOAD["userId"])


@pytest.mark.regression
def test_delete_post():
    """
    QA Risk Covered:
    Verifies that a post can be deleted.

    Passing Test Proves:
    The API accepts delete requests and returns the expected success response within the expected response time.
    """

    response = APIClient.delete("/posts/1")

    assert_status_code(response, 200)
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)