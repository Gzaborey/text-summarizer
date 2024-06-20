from fastapi import FastAPI, HTTPException
import uvicorn
from types import SummaryJSON
from summarizer import TextSummarizer
# from summarizer_downgraded import TextSummarizer
from contextlib import asynccontextmanager
from data_models import TextInput
import logging
from exceptions import InvalidApiException, DownloadingError


# Configure the logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI) -> None:
    """On the start of the server download the model."""

    # Load the NLP model
    try:
        logger.info('    Downloading the model...')
        summarizer = TextSummarizer()
    except TypeError:
        raise InvalidApiException()
    except Exception as e:
        logger.error(f'  Error during model downloading: {e}')
        try:
            logger.info('    Will try to download the default model...')
            summarizer = TextSummarizer(model_id='sshleifer/distilbart-cnn-12-6')
        except Exception:
            raise DownloadingError
    application.state.model = summarizer
    logger.info('    Model downloaded and ready!')
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/summarize")
async def summarize_text(request: TextInput) -> SummaryJSON:
    try:
        summary = app.state.model(request.text)
        result = SummaryJSON
        result.summary = summary
        return result
    except Exception as e:
        logger.error(f"Error during summarization: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
