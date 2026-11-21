from google.genai import errors
from dotenv import load_dotenv
from google import genai
from pydantic import ValidationError

from schemas import Invoice
from response_validator import validate_invoice_response
from prompts import INVOICE_PROMPT_TEMPLATE


def main():

    # Step 1: Load the API key
    load_dotenv()

    # Step 2: Get invoice text
    invoice_text = input("Enter your invoice text:\n").strip()

    if not invoice_text:
        print("Error: Invoice text cannot be empty.")
        return

    # Step 3: Prepare the prompt
    prompt = INVOICE_PROMPT_TEMPLATE.format(
        invoice_text=invoice_text
    )

    # Step 4: Connect to Gemini and extract data
    try:
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": Invoice,
            },
        )

        # Step 5: Validate the response
        invoice = validate_invoice_response(response.text)

        # Step 6: Display the extracted JSON
        print("\nExtracted Invoice JSON:")
        print(invoice.model_dump_json(indent=2))

    except ValidationError as error:
        print("\nInvoice validation failed:")
        print(error)

    except errors.APIError as error:
        print("\nGemini API Error:")
        print(f"Status Code: {error.code}")
        print(f"Message: {error.message}")

    except Exception as error:
        print("\nAn error occurred while processing the invoice:")
        print(error)


if __name__ == "__main__":
    main()