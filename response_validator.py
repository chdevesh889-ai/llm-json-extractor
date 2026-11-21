from schemas import Invoice


def validate_invoice_response(response_text: str) -> Invoice:
    """
    Convert a JSON response into an Invoice object
    and validate its fields.
    """

    # Check whether the response is empty
    if not response_text:
        raise ValueError("Gemini returned an empty response.")

    # Validate the JSON using Pydantic
    invoice = Invoice.model_validate_json(response_text)

    return invoice