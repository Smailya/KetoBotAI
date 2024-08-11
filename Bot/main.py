import openai
import time

openai.api_key = "add your own api key generated from open ai"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant knowledgeable about ketogenic diets, nutrition, and food-related information. Provide detailed information about food items, including their calories, protein, carbs, and whether they are keto-friendly or not. If the food is not keto-friendly, explain why or suggest alternatives."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError as e:
        print("Rate limit error:", e)
        time.sleep(60)  # Wait for a minute before retrying
        return "Sorry, the service is currently unavailable. Please try again later."

if __name__ == "__main__":
    print("Hello! I’m Keton, your personalized keto diet assistant.")
    print("Ask me anything about ketogenic diets and nutrition!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
