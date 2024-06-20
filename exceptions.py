from fastapi import HTTPException


class InvalidApiException(HTTPException):
    def __init__(self,
                 status_code=401,
                 detail=
                 " You are probably using TextSummarizer from summarizer_downgraded module."
                 " Provide a correct HuggingFace API token."
                 " It can be claimed here: https://huggingface.co/settings/tokens"
                 ):
        super().__init__(status_code=status_code, detail=detail)


class DownloadingError(Exception):
    def __init__(self,
                 message="Unable to download a model from Hugging Face Hub."
                 ):
        self.message = message
        super().__init__(self.message)
