from prompts import INVOICE_PROMPT_TEMPLATE


def test_invoice_text_is_inserted():
    invoice_text = "Invoice Number: INV-450\nVendor: Krishna Computers"

    prompt = INVOICE_PROMPT_TEMPLATE.format(
        invoice_text=invoice_text
    )

    assert invoice_text in prompt


def test_prompt_contains_extraction_instructions():
    prompt = INVOICE_PROMPT_TEMPLATE.format(
        invoice_text="Sample invoice"
    )

    assert "invoice_number" in prompt
    assert "vendor" in prompt
    assert "total_amount" in prompt


def test_invoice_placeholder_is_replaced():
    prompt = INVOICE_PROMPT_TEMPLATE.format(
        invoice_text="Sample invoice"
    )

    assert "{invoice_text}" not in prompt