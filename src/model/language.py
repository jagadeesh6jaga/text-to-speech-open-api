from pydantic import BaseModel, validator


class Language(BaseModel):
    sourceLanguage: str

    @validator('sourceLanguage', pre=True)
    def blank_string_in_language(cls, value, field):
        if value == "":
            raise ValueError('sourceLanguage cannot be empty')
        return value
        
class TranslitLanguage(BaseModel):
    sourceLanguage: str
    targetLanguage: str

    @validator('sourceLanguage', pre=True)
    def blank_string_in_sourceLanguage(cls, value, field):
        if value == "":
            raise ValueError('sourceLanguage cannot be empty')
        return value

    @validator('targetLanguage', pre=True)
    def blank_string_in_targetLanguage(cls, value, field):
        if value == "":
            raise ValueError('targetLanguage cannot be empty')
        return value
