import streamlit as st

st.title("🧠 Eonra – Brain-Inspired Reasoning System")

# Use Streamlit session state to store memory
if "last_topic" not in st.session_state:
    st.session_state.last_topic = None

user_input = st.text_input("💬 Ask Eonra a question:")

def eonra_reasoning(question):
    question = question.lower()
    trace = []
    follow_up = ""
    topic = None

    if "ai" in question:
        topic = "Artificial Intelligence"
        trace.append("→ Detected keyword: 'ai'")
        response = "🤖 AI stands for Artificial Intelligence – making machines think like humans."
        follow_up = "Want to explore how AI is used in real-world apps?"

    elif "python" in question:
        topic = "Python Programming"
        trace.append("→ Detected keyword: 'python'")
        response = "🐍 Python is a beginner-friendly programming language used in AI, web, and automation."
        follow_up = "Would you like a Python project idea to try?"

    elif "internship" in question:
        topic = "Career Advice"
        trace.append("→ Detected keyword: 'internship'")
        response = "🎯 Internships help you apply your learning in real companies and improve your resume."
        follow_up = "Need tips on how to find CPT-eligible internships?"

    else:
        trace.append("→ No clear keyword found")
        if st.session_state.last_topic:
            response = f"🤔 Not sure what you meant. Are you asking a follow-up about **{st.session_state.last_topic}**?"
        else:
            response = "🔍 I'm still learning! Try asking about AI, Python, or internships."

    # Save topic to memory
    if topic:
        st.session_state.last_topic = topic

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
