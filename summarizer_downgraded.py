from langchain_community.llms import HuggingFaceHub
from langchain_core.output_parsers import StrOutputParser
from API_token_authentication import HUGGINGFACEHUB_API_TOKEN


class TextSummarizer:
    """A custom text summarizer class."""

    def __init__(self,
                 model_id='sshleifer/distilbart-cnn-12-6',
                 min_new_tokens=20,
                 max_new_tokens=100,
                 max_length=50,
                 huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
                 ):
        """
        :param model_id: Copy and paste the repo_id from HuggingFace hub to choose a desired model \n
        (https://huggingface.co/models?pipeline_tag=summarization). Default is 'sshleifer/distilbart-cnn-12-6'.

        :param min_new_tokens: This parameter specifies the minimum number of new tokens to be generated in the summary.
            It ensures that the generated summary has at least this many new tokens.

        :param max_new_tokens: This parameter specifies the maximum number of new tokens to be generated in the summary.
            It controls the upper limit of the summary length.

        :param max_length:  This parameter specifies the maximum length of the input sequence for the model.
         It ensures that the input text is truncated or padded to this length.

        :param huggingfacehub_api_token: Copy and paste your HuggingFaceHub API token
         from https://huggingface.co/settings/tokens.
        """

        # Initialize the model
        self.model = HuggingFaceHub(
            repo_id=model_id,
            model_kwargs={'max_length': max_length,
                          'max_new_tokens': max_new_tokens,
                          'min_new_tokens': min_new_tokens},
            huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
        )

        # Initialize the LangChain chain
        self.chain = self.model | StrOutputParser()

    def __call__(self, text: str) -> str:
        return self.chain.invoke(text)
