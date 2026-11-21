# Structured LLM Prompt Pipeline & JSON Extractor

A Python-based application that uses Google's Gemini API to extract structured information from unstructured invoice text and convert it into validated JSON.

## Project Overview

This project demonstrates how Large Language Models (LLMs) can be integrated with Python to automate invoice information extraction.

The application uses parameterized prompt templates, Gemini's structured output capabilities, and Pydantic validation to generate consistent JSON responses.

## Features

- Extracts structured data from unstructured invoice text.
- Uses reusable, parameterized prompt templates.
- Integrates with Google's Gemini API.
- Generates structured JSON responses.
- Validates extracted information using Pydantic.
- Handles missing invoice fields using `null`.
- Rejects invalid amounts and empty text fields.
- Handles Gemini API errors.
- Includes automated tests using pytest.

## Technologies Used

- **Python 3.11**
- **Google Gemini API**
- **Google GenAI Python SDK**
- **Pydantic**
- **python-dotenv**
- **pytest**

## Extracted Invoice Fields

| Field | Description |
|---|---|
| invoice_number | Invoice identification number |
| vendor | Vendor or company name |
| date | Invoice date |
| total_amount | Total invoice amount |
| tax | Tax amount |

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/chdevesh889-ai/llm-json-extractor.git
cd llm-json-extractor
```

Replace `<your-repository-url>` with the actual GitHub repository URL after publishing the project.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace the placeholder with your own Gemini API key.

Never commit your `.env` file or API key to GitHub.

## Running the Application

Execute:

```bash
python extract_invoice.py
```

Enter invoice text when prompted.

### Example Input

```text
Invoice Number: INV-450; Vendor: Krishna Computers; Date: 12 August 2026; Total Amount: 25000; Tax: 4500
```

### Example JSON Output

```json
{
  "invoice_number": "INV-450",
  "vendor": "Krishna Computers",
  "date": "2026-08-12",
  "total_amount": 25000.0,
  "tax": 4500.0
}
```

This is an illustrative example, not a guarantee of identical output for every Gemini response.

## Running Automated Tests

Run all tests:

```bash
pytest -v
```

The project includes tests for:

- Invoice schema validation
- Prompt template formatting
- JSON response validation
- Empty input handling
- Simulated Gemini API errors

The existing automated tests use local data and mocks rather than making live Gemini API requests.

## Project Workflow

```text
User Invoice Text
       |
       v
Parameterized Prompt Template
       |
       v
Google Gemini API
       |
       v
Structured JSON Response
       |
       v
Pydantic Validation
       |
       v
Validated Invoice JSON
```

## Security

- API credentials are stored in environment variables.
- The `.env` file is excluded from version control.
- Invoice text is treated as data rather than instructions.
- API errors are handled without exposing the API key.

## Future Improvements

- Support extracting information from invoice PDFs.
- Add batch invoice processing.
- Build a web interface.
- Export validated data to CSV.
- Add more comprehensive date and business-rule validation.

## Project Status

Core invoice extraction, response validation, error handling, and automated testing have been implemented.

## License

MIT License (if included in the repository).
