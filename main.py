import sys
import time
from src.classifier import classify_intent
from src.router import route_and_respond
from src.logger import log_request

def process_message(message: str, silent=False):
    """Processes a single message through the intent router pipeline."""
    if not silent:
        print(f"\n--- Processing Message: {message} ---")
    
    # 1. Classify
    intent_data = classify_intent(message)
    if not silent:
        print(f"Detected Intent: {intent_data['intent']} (Confidence: {intent_data['confidence']})")
    
    # 2. Route and Respond
    response = route_and_respond(message, intent_data)
    if not silent:
        print(f"AI Response:\n{response}")
    
    # 3. Log
    log_request(
        intent=intent_data["intent"],
        confidence=intent_data["confidence"],
        user_message=message,
        final_response=response
    )
    
    return intent_data, response

def run_tests():
    """Runs the predefined test cases."""
    test_messages = [
        "how do i sort a list of objects in python?",
        "explain this sql query for me",
        "This paragraph sounds awkward, can you help me fix it?",
        "I'm preparing for a job interview, any tips?",
        "what's the average of these numbers: 12, 45, 23, 67, 34",
        "hey"
    ]
    
    print("Running 6 test messages...")
    for msg in test_messages:
        process_message(msg, silent=False)
        time.sleep(15)  # Avoid rate limits
    print("\nTests completed. Check route_log.jsonl for results.")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
        return

    print("AI Intent Router CLI (Type 'exit' to quit, '--test' to run battery)")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        if user_input == "--test":
            run_tests()
            continue
        if not user_input:
            continue
            
        process_message(user_input)

if __name__ == "__main__":
    main()