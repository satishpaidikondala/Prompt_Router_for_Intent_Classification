from .llm_client import llm_client
from .prompts import SYSTEM_PROMPTS

def route_and_respond(message: str, intent_data: dict) -> str:
    """
    Routes the message to the appropriate expert persona and returns the response.
    """
    intent = intent_data.get("intent", "unclear")
    confidence = intent_data.get("confidence", 0.0)

    # Confidence threshold or unclear intent
    if confidence < 0.7 or intent == "unclear":
        return "I'm not exactly sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"

    system_prompt = SYSTEM_PROMPTS.get(intent)
    if not system_prompt:
        return "I'm sorry, I couldn't find a specialized expert for that request. Could you please clarify?"

    try:
        response = llm_client.generate(message, system_instruction=system_prompt)
        return response
    except Exception as e:
        print(f"Routing/Response error: {e}")
        return "I encountered an error while consulting the expert. Please try again."
