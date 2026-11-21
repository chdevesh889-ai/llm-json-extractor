from unittest.mock import patch
from extract_invoice import main


def test_empty_invoice_input(capsys):
    with patch("builtins.input", return_value=""):
        main()

    captured = capsys.readouterr()

    assert "Error: Invoice text cannot be empty." in captured.out


from google.genai import errors


def test_gemini_api_error(capsys):
    fake_error = errors.APIError(
        code=429,
        response_json={
            "error": {
                "code": 429,
                "message": "Resource exhausted",
                "status": "RESOURCE_EXHAUSTED"
            }
        }
    )

    with patch("builtins.input", return_value="Sample invoice"):
        with patch("extract_invoice.genai.Client") as mock_client:
            mock_client.return_value.models.generate_content.side_effect = fake_error

            main()

    captured = capsys.readouterr()

    assert "Gemini API Error:" in captured.out
    assert "Status Code: 429" in captured.out
    assert "Resource exhausted" in captured.out