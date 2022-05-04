from fastapi import APIRouter, HTTPException, Response, status

from src import log_setup
from src.application.tts_preprocess import infer_tts_request ,infer_transliterate_request
from src.model.tts_request import TTSRequest ,TransliterationRequest
from src.model.tts_response import TTSFailureResponse , TransliterationFailureResponse


LOGGER = log_setup.get_logger(__name__)
router = APIRouter()


@router.post("/")
async def tts(request: TTSRequest, response: Response):
    LOGGER.info(f'TTS request {request}')
    try:
        infer_response = infer_tts_request(request)
        return infer_response
    except NotImplementedError as e:
        LOGGER.exception('Failed to infer http exception %s', e)
        response.status_code = status.HTTP_404_NOT_FOUND
        return TTSFailureResponse(status_text=str(e))
    except Exception as e:
        LOGGER.exception('Failed to infer %s', e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return TTSFailureResponse(status_text=f'Failed to process request {str(e)}')

@router.post("/get_transliteration")
async def transliteration(request: TransliterationRequest, response: Response):
    LOGGER.info(f'Transliteration request {request}')
    try:
        infer_response = infer_transliterate_request(request)
        return infer_response
    except NotImplementedError as e:
        LOGGER.exception('Failed to infer http exception %s', e)
        response.status_code = status.HTTP_404_NOT_FOUND
        return TransliterationFailureResponse(status_text=str(e))
    except Exception as e:
        LOGGER.exception('Failed to infer %s', e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return TransliterationFailureResponse(status_text=f'Failed to process request {str(e)}')