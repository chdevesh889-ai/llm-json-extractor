from google.genai import errors


def test_api_error_has_status_code():
    error = errors.APIError(
        code=429,
        response_json={
            "error": {
                "code": 429,
                "message": "Resource exhausted",
                "status": "RESOURCE_EXHAUSTED"
            }
        }
    )

    assert error.code == 429


def test_api_error_can_be_caught():
    error = errors.APIError(
        code=429,
        response_json={
            "error": {
                "code": 429,
                "message": "Resource exhausted",
                "status": "RESOURCE_EXHAUSTED"
            }
        }
    )

    try:
        raise error

    except errors.APIError as caught_error:
        assert caught_error.code == 429
        assert caught_error.message == "Resource exhausted"