import streamlit as st
from utils import storage

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Language Tutor - HACK O OCTO 2.0",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(45deg, #2196F3, #00BCD4);
        color: white;
        border: none;
        padding: 15px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .stTitle {
        color: #1a237e;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 30px;
    }
    .stSubheader {
        color: #0d47a1;
        font-size: 1.8em;
        margin-top: 30px;
    }
    .hackathon-badge {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9em;
        display: inline-block;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- Load Lesson Plan ---
lesson_plan = storage.load_lesson_plan()

# --- Calculate Progress ---
total_tasks = sum(len(week['assignments']) for week in lesson_plan)
completed_tasks = sum(
    1 for week in lesson_plan for task in week['assignments'] if task.get('completed', False)
)

progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

# --- Render Sidebar ---
from sidebar import render_sidebar
render_sidebar()

# --- Main Page Content ---
st.title("🎓 AI Language Tutor")
st.markdown("""
    <div style='text-align: center;'>
        <div class="hackathon-badge">🚀 HACK O OCTO 2.0</div>
        <div style='color: #546e7a; font-size: 1.2em; margin-bottom: 30px;'>
            Your personalized AI-powered language learning companion
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💬 AI Tutor Chat", key="main_chatbot"):
        st.switch_page("pages/chatbot.py")
with col2:
    if st.button("🌐 Translator", key="main_translator"):
        st.switch_page("pages/translator.py")
with col3:
    if st.button("📚 Vocabulary Builder", key="main_vocab"):
        st.switch_page("pages/vocab.py")
with col4:
    if st.button("📖 Lesson Plans", key="main_lesson_plan"):
        st.switch_page("pages/lesson_plan.py")

# Additional Navigation Row
col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("🗣️ Pronunciation", key="main_pronunciation"):
        st.switch_page("pages/pronunciation.py")
with col6:
    if st.button("📝 Quizzes", key="main_quizzes"):
        st.switch_page("pages/quizzes.py")
with col7:
    if st.button("📊 Analytics", key="main_analytics"):
        st.switch_page("pages/analytics.py")
with col8:
    if st.button("📜 History", key="main_history"):
        st.switch_page("pages/history.py")

# --- Modern Progress Tracker ---
st.subheader("📊 Learning Progress")

# Custom CSS for Modern Progress Bar
st.markdown(f"""
    <style>
    .progress-container {{
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px 0;
    }}
    .progress-bar {{
        height: 25px;
        background: linear-gradient(45deg, #e3f2fd, #bbdefb);
        border-radius: 12px;
        overflow: hidden;
        position: relative;
    }}
    .progress-fill {{
        height: 100%;
        background: linear-gradient(45deg, #2196F3, #00BCD4);
        width: {progress}%;
        transition: width 0.5s ease-in-out;
        border-radius: 12px;
    }}
    .progress-text {{
        text-align: center;
        color: #546e7a;
        font-size: 1.1em;
        margin-top: 10px;
    }}
    </style>

    <div class="progress-container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
        <div class="progress-text">
            {completed_tasks} of {total_tasks} lessons completed ({progress:.1f}%)
        </div>
    </div>
""", unsafe_allow_html=True)

# Dynamic Encouragement Messages
st.markdown("""
    <style>
    .encouragement {{
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        font-size: 1.2em;
    }}
    </style>
""", unsafe_allow_html=True)

if progress == 0:
    st.markdown("""
        <div class="encouragement" style="background: #e3f2fd; color: #1565c0;">
            🎯 Ready to begin your language learning journey? Let's get started!
        </div>
    """, unsafe_allow_html=True)
elif progress < 50:
    st.markdown("""
        <div class="encouragement" style="background: #e8f5e9; color: #2e7d32;">
            🌟 Great progress! You're making excellent strides in your learning journey!
        </div>
    """, unsafe_allow_html=True)
elif progress < 100:
    st.markdown("""
        <div class="encouragement" style="background: #fff3e0; color: #ef6c00;">
            🚀 You're almost there! Keep pushing towards your language goals!
        </div>
    """, unsafe_allow_html=True)
else:
    st.balloons()
    st.markdown("""
        <div class="encouragement" style="background: #f3e5f5; color: #7b1fa2;">
            🎉 Congratulations! You've completed all your lessons! Time to set new goals!
        </div>
    """, unsafe_allow_html=True)

# Footer with Azure Services Badge
st.markdown("""
    <div style='text-align: center; margin-top: 40px;'>
        <img src='https://img.shields.io/badge/Powered%20by-Azure%20AI%20Services-blue' alt='Azure AI Services'>
        <img src='https://img.shields.io/badge/Azure%20Translator-Enabled-green' alt='Azure Translator'>
        <img src='https://img.shields.io/badge/Azure%20Speech-Enabled-green' alt='Azure Speech'>
    </div>
""", unsafe_allow_html=True)
