from openai import OpenAIError
from fastapi import FastAPI, Form, HTTPException

from edu_assistant.assistant import create_response
from edu_assistant.config import RoleType, TemplateType

app = FastAPI()


@app.post('/ask')
def ask(
    role: RoleType = Form(),
    template: TemplateType = Form(),
    question: str = Form(examples=["Ты кто?"]),
) -> str:
    """Ask question to educational assistant."""
    try:
        return create_response(
            llm_key="api",
            role=role,
            template=template,
            prompt=question,
        )
    except OpenAIError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error
