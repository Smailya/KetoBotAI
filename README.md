# Keton - AI Keto Diet Assistant

## Overview

Welcome to **Keton**, your AI-powered assistant designed to support your ketogenic diet journey! Keton provides detailed nutritional information and personalized advice on keto-friendly foods, helping you make informed dietary choices with ease.

## Features

- **Food Information:** Get comprehensive details about calories, protein, carbohydrates, and more.
- **Keto-Friendly Guidance:** Instantly know if a food is keto-friendly or receive suggestions for suitable alternatives.
- **Real-Time Interaction:** Engage with Keton in real-time for instant feedback on your keto diet queries.
- **Robust Error Handling:** Handles API rate limit errors gracefully by pausing and retrying to ensure smooth user experience.

## How It Works

Keton leverages OpenAI's **GPT-3.5-turbo** model to understand and respond to your questions about foods and the ketogenic diet. When you ask about a specific food, Keton provides:

- Caloric content  
- Protein and carbohydrate levels  
- Keto-friendliness assessment  
- Suggestions for keto-friendly alternatives if the food is not suitable  

## Getting Started

### Prerequisites

- Python 3.x  
- An OpenAI API key  

### Installation

Install the required Python package:

pip install openai

text

### Usage

1. Set your OpenAI API key in the script:

import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

text

2. Run the assistant:

python main.py

text

3. Interact with Keton by typing your questions about foods and the keto diet.

### Example Interaction

You: Is avocado keto-friendly?
Keton: Avocado is very keto-friendly! It is high in healthy fats, moderate in protein, and low in carbs, making it an excellent choice for a ketogenic diet.

text

## Error Handling

If the OpenAI API rate limit is reached, Keton automatically pauses for 60 seconds before retrying, ensuring uninterrupted and smooth interaction.

## Why This Project Matters

This project merges AI, API integration, and user-facing utility - a combination highly relevant for full-stack engineers building health-tech applications and personalized assistants. It demonstrates:

- Integration and structuring of OpenAI prompts  
- Managing API rate limits with robust error handling  
- Enhancing conversational logic for engaging user experiences  

These skills empower companies to deliver intelligent, scalable, and personalized support, improving customer satisfaction and content relevance.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve Keton’s features and capabilities.

## Contact

For inquiries or suggestions, please reach out to me on [LinkedIn](https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/ismail-cisse/)).

---

Developed by Ismail Cisse 
Empowering ketogenic diet users with AI-driven nutritional insights.
