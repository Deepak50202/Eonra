import streamlit as st

# Initialize memory for recent questions
if "question_history" not in st.session_state:
    st.session_state.question_history = []


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
  
    elif "streamlit" in question:
        topic = "Streamlit"
        trace.append("→ Detected keyword: 'streamlit'")
        response = "📊 Streamlit turns Python scripts into shareable web apps. It’s great for beginners and prototyping."
        follow_up = "Want to learn how to deploy your Streamlit app?"

    elif "resume" in question:
        topic = "Resume Tips"
        trace.append("→ Detected keyword: 'resume'")
        response = "📄 A strong resume should show projects, skills, and relevant certifications clearly."
        follow_up = "Would you like tips for ATS-friendly formatting?"

    elif "project" in question:
        topic = "Project Building"
        trace.append("→ Detected keyword: 'project'")
        response = "🛠 Projects show initiative. Even simple tools like calculators or logic bots are great!"
        follow_up = "Need beginner-friendly project ideas?"

    elif "deploy" in question or "deployment" in question:
        topic = "Deployment"
        trace.append("→ Detected keyword: 'deploy'")
        response = "🚀 You can deploy Python apps using Streamlit Share, Render, or Hugging Face Spaces."
        follow_up = "Want help deploying Eonra online?"

    elif "learn" in question or "learning path" in question:
        topic = "Learning Path"
        trace.append("→ Detected keyword: 'learn'")
        response = "📚 Start with Python basics, build projects, then explore topics like AI, web, or data."
        follow_up = "Need a step-by-step plan based on your goals?"

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
# Button to clear memory
if st.button("🧹 Clear Memory"):
    st.session_state.question_history = []
    st.session_state.last_topic = None
    st.success("Memory cleared. Eonra is ready for a new session!")

if st.button("Think"):
    # Save current question to history
    if user_input:
        st.session_state.question_history.append(user_input)
        # Keep only last 3 questions
        st.session_state.question_history = st.session_state.question_history[-3:]

    # Show recent context
    if st.session_state.question_history:
        st.markdown("### 🧠 Recent Context:")
        for q in st.session_state.question_history:
            st.write(f"• {q}")

    trace_steps, final_answer, followup = eonra_reasoning(user_input)

    st.markdown("### 🧠 Thought Process:")
    for step in trace_steps:
        st.write(step)

    st.markdown("### 🤖 Eonra's Response:")
    st.write(final_answer)

    if followup:
        st.markdown("### 🔄 Follow-Up Suggestion:")
        st.write(followup)
