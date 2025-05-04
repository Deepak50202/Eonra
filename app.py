import streamlit as st

st.title("🧠 Eonra – Brain-Inspired Reasoning")

user_input = st.text_input("💬 Ask Eonra a question:")

def eonra_reasoning(question):
    question = question.lower()
    trace = []
    follow_up = ""

    if "ai" in question or "artificial intelligence" in question:
        trace.append("→ Detected keyword: 'ai'")
        trace.append("→ Matched topic: Artificial Intelligence")
        response = "🤖 AI (Artificial Intelligence) is the field of creating machines that can perform tasks that normally require human intelligence."
        follow_up = "Would you like to learn how AI is used in self-driving cars or healthcare?"

    elif "machine learning" in question or "ml" in question:
        trace.append("→ Detected keyword: 'machine learning'")
        trace.append("→ Matched topic: Machine Learning")
        response = "📊 Machine learning is a part of AI that enables systems to learn and improve from experience without being explicitly programmed."
        follow_up = "Want to see an example of a real ML model like a spam filter or image classifier?"

    elif "python" in question or "programming language" in question:
        trace.append("→ Detected keyword: 'python'")
        trace.append("→ Matched topic: Python Programming")
        response = "🐍 Python is a popular programming language known for its simplicity and is widely used in AI, web development, and automation."
        follow_up = "Would you like a beginner project idea to build with Python?"

    elif "data science" in question or "data analyst" in question:
        trace.append("→ Detected keyword: 'data science'")
        trace.append("→ Matched topic: Data Science")
        response = "📈 Data Science is the process of extracting insights from data using statistics, programming, and machine learning."
        follow_up = "You could explore datasets from Kaggle to practice data science skills!"

    elif "chatgpt" in question or "openai" in question:
        trace.append("→ Detected keyword: 'chatgpt'")
        trace.append("→ Matched topic: Generative AI")
        response = "💬 ChatGPT is a large language model developed by OpenAI that can understand and generate human-like text responses."
        follow_up = "Would you like to try building a chatbot using GPT yourself?"

    elif "internship" in question or "resume" in question:
        trace.append("→ Detected keyword: 'internship'")
        trace.append("→ Matched topic: Career Advice")
        response = "🎯 Internships help you gain real-world experience, build skills, and improve your resume."
        follow_up = "Want tips on how to find internships as an international student?"

    elif "eonra" in question:
        trace.append("→ Detected keyword: 'eonra'")
        trace.append("→ Matched topic: Eonra Reasoning System")
        response = "🧠 Eonra is a brain-inspired reasoning engine designed to simulate step-by-step logic."
        follow_up = "Would you like to see how Eonra’s reasoning logic works in layers?"

    else:
        trace.append("→ No known keywords detected")
        trace.append("→ Unable to match topic")
        response = "🔍 I'm still learning. Try asking about AI, Python, data science, ChatGPT, or internships!"
        follow_up = "Or give me feedback so I can improve!"

    return trace, response, follow_up

if st.button("Think"):
    trace_steps, final_answer, followup = eonra_reasoning(user_input)

    st.markdown("### 🧠 Thought Process:")
    for step in trace_steps:
        st.write(step)

    st.markdown("### 🤖 Eonra's Response:")
    st.write(final_answer)

    if followup:
        st.markdown("### 🔄 Follow-Up Suggestion:")
        st.write(followup)
