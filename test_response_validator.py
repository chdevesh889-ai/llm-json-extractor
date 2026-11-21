import pytest
from pydantic import ValidationError

from response_validator import validate_invoice_response


def test_valid_invoice_response():
    response = """
    {
        "invoice_number": "INV-450",
        "vendor": "Krishna Computers",
        "date": "2026-08-12",
        "total_amount": 25000,
        "tax": 4500
    }
    """

    invoice = validate_invoice_response(response)

    assert invoice.invoice_number == "INV-450"
    assert invoice.vendor == "Krishna Computers"
    assert invoice.total_amount == 25000


def test_negative_amount_is_rejected():
    response = """
    {
        "invoice_number": "INV-450",
        "vendor": "Krishna Computers",
        "date": "2026-08-12",
        "total_amount": -25000,
        "tax": 4500
    }
    """

    with pytest.raises(ValidationError):
        validate_invoice_response(response)


def test_invalid_json_is_rejected():
    response = "This is not valid JSON"

    with pytest.raises(ValidationError):
        validate_invoice_response(response)


def test_empty_response_is_rejected():
    response = ""

    with pytest.raises(ValueError):
        validate_invoice_response(response)