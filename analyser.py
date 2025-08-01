from typing import Type
from models import ChatResponse
from openai import OpenAI
from pydantic import BaseModel
from prompts_templates import JOB_QUESTION_WITH_CV_PROMPT_EN

class CVAnalyzer:
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def _call_openai(self, prompt: str, response_model: Type[BaseModel]) -> BaseModel:
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an HR expert specialized in CV and job offer analysis."},
                {"role": "user", "content": prompt}
            ],
            response_format=response_model,
        )
        return response.choices[0].message.parsed

    def answer_job_question(self, cv_text: str, job_offer_text: str, question: str) -> ChatResponse:
        prompt = JOB_QUESTION_WITH_CV_PROMPT_EN.format(cv_text=cv_text, job_offer_text=job_offer_text, question=question)
        return self._call_openai(prompt, ChatResponse)