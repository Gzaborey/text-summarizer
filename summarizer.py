from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM


class TextSummarizer:
    """A custom text summarizer class."""

    def __init__(self,
                 model_id='sshleifer/distilbart-cnn-12-6',
                 min_new_tokens=20,
                 max_new_tokens=100,
                 max_length=50,
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
        """

        # Initialize the model
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

        # Initialize the tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_id,
                                                       truncation=True,
                                                       )

        # Create a pipeline
        self.pipe = pipeline(task="summarization",
                             model=self.model,
                             tokenizer=self.tokenizer,
                             min_new_tokens=min_new_tokens,
                             max_new_tokens=max_new_tokens,
                             max_length=max_length,
                             )

        # Initialize the LangChain pipeline
        self.hf = HuggingFacePipeline(pipeline=self.pipe)

    def __call__(self, text: str) -> str:
        return self.hf.invoke(text)
