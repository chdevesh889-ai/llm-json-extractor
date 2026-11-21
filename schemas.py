from pydantic import BaseModel, Field, field_validator


class Invoice(BaseModel):
    invoice_number: str | None = Field(
        description="The invoice number, or null if missing"
    )

    vendor: str | None = Field(
        description="The vendor name, or null if missing"
    )

    date: str | None = Field(
        description="The invoice date in YYYY-MM-DD format, or null if missing"
    )

    total_amount: float | None = Field(
        description="The total invoice amount, or null if missing"
    )

    tax: float | None = Field(
        description="The tax amount, or null if missing"
    )

    @field_validator("invoice_number", "vendor")
    @classmethod
    def validate_text_fields(cls, value):
        if value is not None and not value.strip():
            raise ValueError("This field cannot be empty.")
        return value

    @field_validator("total_amount", "tax")
    @classmethod
    def validate_amounts(cls, value):
        if value is not None and value < 0:
            raise ValueError("Amount cannot be negative.")
        return value