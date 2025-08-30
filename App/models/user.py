from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    phoneNumber:str