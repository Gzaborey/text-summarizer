class DownloadingError(Exception):
    def __init__(self,
                 message="Unable to download a model from Hugging Face Hub."
                 ):
        self.message = message
        super().__init__(self.message)
