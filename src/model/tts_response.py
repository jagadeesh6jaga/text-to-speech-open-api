from typing import List

from pydantic import BaseModel

from src.model.language import Language


class AudioFile(BaseModel):
    audioContent: str


class AudioConfig(BaseModel):
    language: Language
    audioFormat: str = 'wav'
    encoding: str = 'base64'
    samplingRate: int = 22050


class TTSResponse(BaseModel):
    audio: List[AudioFile]
    config: AudioConfig


class TTSFailureResponse(BaseModel):
    status: str = 'ERROR'
    status_text: str

class source_target_text(BaseModel):
    source: str
    target: str

class Status(BaseModel):
    statusCode: int
    message: str

class TranslitResponse(BaseModel):
    output : List[source_target_text]
    status: Status

class TransliterationFailureResponse(BaseModel):
    status: str = 'ERROR'
    status_text: str
