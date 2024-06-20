from pydantic import BaseModel


class TextInput(BaseModel):
    """A data model to represent an input to the TextSummarizer."""

    text: str
