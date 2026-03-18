import json
import re
from .llm_client import llm_client

CLASSIFIER_PROMPT = """Your task is to classify the user's intent. Based on the user message below, choose one of the following labels: code, data, writing, career, unclear. Respond with a single JSON object containing two keys: 'intent' (the label you chose) and 'confidence' (a float from 0.0 to 1.0, representing your certainty). Do not provide any other text or explanation."""

def classify_intent(message: str) -> dict:
    """
    Classifies the user's intent using a lightweight LLM call.
    Returns a dictionary with 'intent' and 'confidence'.
    """
    try:
        prompt = f"{CLASSIFIER_PROMPT}\n\nUser Message: {message}"
        response_text = llm_client.generate(prompt)
        
        # Extract JSON using regex in case LLM adds markdown or extra text
        match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if match:
            parsed = json.loads(match.group())
            return {
                "intent": parsed.get("intent", "unclear"),
                "confidence": float(parsed.get("confidence", 0.0))
            }
            
    except Exception as e:
        print(f"Classification error: {e}")
        
    # Default fallback
    return {"intent": "unclear", "confidence": 0.0}
