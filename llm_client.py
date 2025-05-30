import re
from huggingface_hub import InferenceClient


API_KEY = "I WILL PROVIDE IT SEPARATELY"


def send_request(client, message):
    try:
        completion = client.chat.completions.create(
            model="Qwen/Qwen3-32B",
            messages=[{"role": "user", "content": message}],
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"


def clean_thought_process_from_response(response):
    cleaned = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
    return cleaned.strip()


def chat():
    client = InferenceClient(provider="cerebras", api_key=API_KEY)
    print("Welcome to Cerebras Chat Bot")
    
    clean_enabled = input("Do you want to hide the thought process behind model' decision? ").strip().lower() in ["yes", "y"]

    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            response = send_request(client, user_input)

            if "Error: 401" in response:
                raise Exception("unauthorized")

            if clean_enabled:
                response = clean_thought_process_from_response(response)

            print("Assistant:", response)
    except Exception as e:
            print(f"oops, something went wrong, check message: {str(e)}")

if __name__ == "__main__":
    chat()
