import pytest
from pydantic import ValidationError

from schemas import Invoice


def test_valid_invoice():
    invoice = Invoice(
        invoice_number="INV-450",
        vendor="Krishna Computers",
        date="2026-08-12",
        total_amount=25000,
        tax=4500,
    )

    assert invoice.invoice_number == "INV-450"
    assert invoice.vendor == "Krishna Computers"
    assert invoice.total_amount == 25000


def test_missing_fields_are_allowed():
    invoice = Invoice(
        invoice_number="INV-301",
        vendor="ABC Technologies",
        date=None,
        total_amount=5000,
        tax=None,
    )

    assert invoice.date is None
    assert invoice.tax is None


def test_negative_amount_is_rejected():
    with pytest.raises(ValidationError):
        Invoice(
            invoice_number="INV-450",
            vendor="Krishna Computers",
            date="2026-08-12",
            total_amount=-25000,
            tax=4500,
        )


def test_empty_vendor_is_rejected():
    with pytest.raises(ValidationError):
        Invoice(
            invoice_number="INV-450",
            vendor="   ",
            date="2026-08-12",
            total_amount=25000,
            tax=4500,
        )


def test_invalid_amount_type_is_rejected():
    with pytest.raises(ValidationError):
        Invoice(
            invoice_number="INV-450",
            vendor="Krishna Computers",
            date="2026-08-12",
            total_amount="not a number",
            tax=4500,
        )