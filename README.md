# Eonra – Brain-Inspired AI Reasoning System

Eonra is a logic-driven AI assistant that simulates how the human brain reasons, recalls, and responds. It combines structured topic recognition with fallback support using OpenAI's GPT-3.5 API for open-ended questions.

This project was built as a full-stack MVP to showcase skills in Python development, AI integration, deployment, and user-focused design.

---

## Live Demo

[Launch Eonra on Streamlit](https://deepak50202-eonra-app-kcubv5.streamlit.app)  
[View on GitHub](https://github.com/Deepak50202/Eonra)

---

## Features

- Logic-based keyword detection and topic mapping  
- Short-term memory for recent user queries  
- Smart follow-up suggestions based on previous topics  
- GPT-3.5 Turbo fallback for unmatched questions  
- Starter prompt buttons for first-time users  
- Session summary with topic coverage  
- Clear memory button to reset state  
- Feedback interface for user input (Yes/No)  
- Related topic recommendations  

---

## Why I Built This

I wanted to move beyond static chatbots and create something that reasons like a human. Eonra helps users understand not just answers, but how answers are formed — and uses GPT only when needed.

This was also a practical way to apply and learn:

- Python and Streamlit  
- API Integration (OpenAI)  
- Git and GitHub workflow  
- State management and memory logic  
- Clean, minimal UI design  
- Public cloud deployment with environment secrets  

---

## Tech Stack

- Python 3  
- Streamlit  
- OpenAI API (v1.0 SDK, GPT-3.5 Turbo)  
- Git & GitHub  
- Streamlit Cloud (Deployment)  

---

## How It Works

1. Detects keywords like “AI”, “Python”, “Resume”, etc.  
2. If matched → returns a prebuilt logical answer and follow-up.  
3. If not matched → sends the question to GPT-3.5 via OpenAI.  
4. Shows memory trace, session summary, and related links.  

---

## Deployment Notes

- The app is deployed on Streamlit Cloud  
- Secrets like the OpenAI API key are safely stored in `.streamlit/secrets.toml`  
- A funded OpenAI account is required to enable GPT responses  

---

## Future Enhancements

- Long-term memory per user  
- Login/authentication for personalized sessions  
- Convert into a full SaaS platform  
- Multi-model GPT switching and key customization  

---

## Disclaimer

This app uses the OpenAI API under a personal developer account and may stop working when API limits are reached. Responses are AI-generated and should be independently verified for critical use.

---

## Connect

[GitHub – Deepak50202](https://github.com/Deepak50202/Eonra)  
[LinkedIn – Deepak Enjapuri](https://linkedin.com/in/deepakenjapuri)
