import pytest

from config import MAX_RESPONSE_TIME_SECONDS
from utils.api_client import APIClient
from utils.assertions import (
    assert_status_code,
    assert_json_field_exists,
    assert_schema,
    assert_content_type,
    assert_response_time_less_than
)
from schemas.post_schema import POST_SCHEMA


@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_posts():
    """
    QA Risk Covered:
    Verifies that the posts endpoint is available and returns a list of records.

    Passing Test Proves:
    The API can return post data successfully in JSON format within the expected response time.
    """

    response = APIClient.get("/posts")

    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)

    response_json = response.json()

    assert isinstance(response_json, list)
    assert len(response_json) > 0

    first_post = response_json[0]

    assert_json_field_exists(first_post, "userId")
    assert_json_field_exists(first_post, "id")
    assert_json_field_exists(first_post, "title")
    assert_json_field_exists(first_post, "body")

    assert_schema(first_post, POST_SCHEMA)


@pytest.mark.smoke
@pytest.mark.regression
def test_get_single_post():
    """
    QA Risk Covered:
    Verifies that a valid post ID returns the correct post object and expected schema.

    Passing Test Proves:
    The API can retrieve an individual post by ID and return JSON with the expected response structure within the expected response time.
    """

    response = APIClient.get("/posts/1")

    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)

    response_json = response.json()

    assert response_json["id"] == 1
    assert_json_field_exists(response_json, "userId")
    assert_json_field_exists(response_json, "title")
    assert_json_field_exists(response_json, "body")

    assert_schema(response_json, POST_SCHEMA)


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_multiple_posts_by_id(post_id):
    """
    QA Risk Covered:
    Verifies that multiple valid post IDs return valid post records.

    Passing Test Proves:
    The API consistently retrieves individual posts across different IDs within the expected response time.
    """

    response = APIClient.get(f"/posts/{post_id}")

    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)

    response_json = response.json()

    assert response_json["id"] == post_id
    assert_json_field_exists(response_json, "userId")
    assert_json_field_exists(response_json, "title")
    assert_json_field_exists(response_json, "body")

    assert_schema(response_json, POST_SCHEMA)


@pytest.mark.regression
@pytest.mark.parametrize("invalid_post_id", [999999, 0, -1])
def test_get_invalid_post_ids(invalid_post_id):
    """
    QA Risk Covered:
    Verifies that invalid post IDs are handled correctly.

    Passing Test Proves:
    The API returns 404 for post records that do not exist within the expected response time.
    """

    response = APIClient.get(f"/posts/{invalid_post_id}")

    assert_status_code(response, 404)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)


@pytest.mark.regression
def test_get_post_not_found():
    """
    QA Risk Covered:
    Verifies that the API handles an invalid post ID correctly.

    Passing Test Proves:
    The API returns a proper 404 response for a post that does not exist within the expected response time.
    """

    response = APIClient.get("/posts/999999")

    assert_status_code(response, 404)
    assert_content_type(response, "application/json")
    assert_response_time_less_than(response, MAX_RESPONSE_TIME_SECONDS)