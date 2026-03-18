from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .classifier import classify_intent
from .router import route_and_respond
from .logger import log_request

app = FastAPI(title="AI Intent Router API")

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    intent: str
    confidence: float
    response: str

@app.post("/route", response_model=MessageResponse)
async def route_message(request: MessageRequest):
    try:
        # 1. Classify
        intent_data = classify_intent(request.message)
        
        # 2. Route and Respond
        response_text = route_and_respond(request.message, intent_data)
        
        # 3. Log
        log_request(
            intent=intent_data["intent"],
            confidence=intent_data["confidence"],
            user_message=request.message,
            final_response=response_text
        )
        
        return MessageResponse(
            intent=intent_data["intent"],
            confidence=intent_data["confidence"],
            response=response_text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
