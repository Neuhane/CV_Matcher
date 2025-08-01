from pydantic import BaseModel

class ChatResponse(BaseModel):
    response: str

    def __str__(self):
        return self.response
