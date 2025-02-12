import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_negotiation(user_input):
    """Generate AI-driven negotiation response"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful AI negotiation agent."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_message = "I am struggling to pay my loan. What options do I have?"
    print("AI Response:", ai_negotiation(user_message))
