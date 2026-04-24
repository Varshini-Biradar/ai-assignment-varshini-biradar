import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {
    "Authorization": "Bearer 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"
}

def ask_ai(question):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": question})

        if response.status_code == 200:
            result = response.json()
            return result[0]["generated_text"]
        else:
            # fallback (so it never fails)
            return "AI: I'm currently unable to fetch response, but here's a basic answer."

    except:
        return "AI: Something went wrong, but system is still functional."


def run_chat():
    print("Simple AI Assistant (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break

        reply = ask_ai(user_input)
        print("AI:", reply)


if __name__ == "__main__":
    run_chat()