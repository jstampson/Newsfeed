import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash",
  generation_config=generation_config,
  system_instruction= """You are a leading expert in the field of AI, tech, and science. Your task is to produce fuctually accurate content in outstandingly precise language, such that it is perfectly understandable for a undergraduate student in the respective subject""",
)

def request_gemini(user_prompt): # for testing LLM itself
    response = model.generate_content(user_prompt)
    return response.text


def summarize_news_items(news_items):
    summaries = []

    for item in news_items:
        prompt = build_prompt(item)
        response = model.generate_content(prompt)
        summaries.append(response.text.strip())

    return summaries

def build_prompt(item):
    return (
        f"Summarize this news item in 1-2 clear sentences for a daily AI news update. Feel free add your personal opinion\n"
        f"Source: {item['source']}\n"
        f"Title: {item['title']}\n"
        f"Summary: {item['summary']}\n"
    )

def compose_morning_briefing(news_items):
    prompt = (
        "You're writing a morning AI news audio briefing. "
        "Make it entertaining, and very informative. "
        "Avoid listing every headline. Instead, group related items, make smooth transitions. "
        "Don't make things up. Do not use bullet points. Keep it 300 words max.\n\n"
        "Here are today's news summaries:\n"
    )

    for item in news_items:
        prompt += (
            f"- Source: {item['source']}\n"
            f"  Title: {item['title']}\n"
            f"  Summary: {item['summary']}\n\n"
        )

    response = model.generate_content(prompt)
    return response.text.strip()
