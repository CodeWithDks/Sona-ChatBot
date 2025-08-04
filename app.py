import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import time
import os

# Page configuration
st.set_page_config(
    page_title="Sona - Educational AI Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with modern responsive design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Reset and base styles */
    * {
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
    }
    
    .main .block-container {
        padding: 1rem;
        max-width: 100%;
    }
    
    /* Responsive animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #00f2fe);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        25% { background-position: 100% 50%; }
        50% { background-position: 100% 100%; }
        75% { background-position: 0% 100%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Smooth floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }
    
    /* Pulse animation */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    /* Glow effect */
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.4); }
        50% { box-shadow: 0 0 30px rgba(102, 126, 234, 0.7); }
    }
    
    /* Shimmer effect */
    @keyframes shimmer {
        0% { background-position: -200px 0; }
        100% { background-position: 200px 0; }
    }
    
    /* Main header - responsive */
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: clamp(2.5rem, 6vw, 4rem);
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: float 3s ease-in-out infinite;
        position: relative;
    }
    
    .main-header::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: shimmer 2s infinite;
    }
    
    /* Sub header - responsive */
    .sub-header {
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
        font-size: clamp(1rem, 3vw, 1.4rem);
        margin-bottom: 2rem;
        font-weight: 400;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Developer info - responsive positioning */
    .developer-info {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.9), rgba(118, 75, 162, 0.9));
        color: white;
        padding: 12px 16px;
        border-radius: 20px;
        font-size: 0.8rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        z-index: 1000;
        animation: glow 3s ease-in-out infinite;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        max-width: calc(100vw - 20px);
    }
    
    .developer-info:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    }
    
    /* Social links - responsive */
    .social-links {
        display: flex;
        gap: 8px;
        margin-top: 8px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .social-link {
        color: white;
        text-decoration: none;
        padding: 4px 8px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.15);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 0.75rem;
        white-space: nowrap;
    }
    
    .social-link:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-2px);
        color: white;
        text-decoration: none;
    }
    
    /* Glass morphism containers */
    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: float 2s ease-in-out infinite;
    }
    
    .glass-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* Stats container - responsive grid */
    .stats-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 1.2rem;
        border-radius: 18px;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: float 2s ease-in-out infinite;
        text-align: center;
    }
    
    .stats-container:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* Metrics styling */
    .metric-container {
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .metric-container [data-testid="metric-container"] {
        background: transparent;
        border: none;
        padding: 0;
    }
    
    .metric-container [data-testid="metric-container"] > div {
        color: white !important;
        font-weight: 600;
    }
    
    /* Welcome card - responsive */
    .welcome-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 2rem;
        border-radius: 25px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
        animation: pulse 3s ease-in-out infinite;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .welcome-card h2 {
        font-size: clamp(1.5rem, 4vw, 2rem);
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #fff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .welcome-card p {
        font-size: clamp(1rem, 2.5vw, 1.2rem);
        opacity: 0.9;
    }
    
    /* Feature cards - responsive */
    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 1.5rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.15);
    }
    
    .feature-card h3 {
        font-size: clamp(1.1rem, 3vw, 1.3rem);
        margin-bottom: 0.5rem;
        color: #fff;
    }
    
    .feature-card p {
        font-size: clamp(0.9rem, 2vw, 1rem);
        opacity: 0.9;
        line-height: 1.5;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 1.5rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        animation: float 2.5s ease-in-out infinite;
        color: white;
    }
    
    /* Sidebar text color */
    .sidebar-content h1, .sidebar-content h2, .sidebar-content h3 {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Button styling - responsive */
    .stButton button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        font-size: clamp(0.8rem, 2vw, 1rem) !important;
        min-height: 2.5rem !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
        background: linear-gradient(135deg, #5a6fd8, #6a4190) !important;
    }
    
    /* Input styling */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        color: white !important;
        backdrop-filter: blur(10px) !important;
        padding: 0.75rem 1rem !important;
        font-size: clamp(0.9rem, 2vw, 1rem) !important;
    }
    
    .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
    }
    
    /* Selectbox styling */
    .stSelectbox select {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        color: white !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Slider styling */
    .stSlider {
        padding: 1rem 0;
    }
    
    .stSlider label {
        color: white !important;
        font-weight: 500 !important;
    }
    
    /* Number input styling */
    .stNumberInput input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        color: white !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        margin: 0.5rem 0 !important;
        padding: 1rem !important;
        animation: slideIn 0.3s ease-out !important;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Chat input styling */
    .stChatInput {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 25px !important;
        padding: 0.5rem !important;
    }
    
    /* Footer styling */
    .footer {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .footer h3 {
        font-size: clamp(1.2rem, 3vw, 1.5rem);
        margin-bottom: 1rem;
    }
    
    .footer p {
        font-size: clamp(0.9rem, 2vw, 1rem);
        margin: 0.5rem 0;
        opacity: 0.9;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 0.5rem;
        }
        
        .developer-info {
            position: relative;
            bottom: auto;
            right: auto;
            margin: 1rem auto;
            max-width: 100%;
        }
        
        .glass-container, .stats-container, .welcome-card, .feature-card {
            margin: 0.5rem 0;
            padding: 1rem;
        }
        
        .social-links {
            gap: 5px;
        }
        
        .social-link {
            font-size: 0.7rem;
            padding: 3px 6px;
        }
        
        /* Ensure proper spacing on mobile */
        .element-container {
            margin-bottom: 1rem;
        }
    }
    
    @media (max-width: 480px) {
        .main-header {
            font-size: 2rem;
        }
        
        .sub-header {
            font-size: 1rem;
        }
        
        .developer-info {
            font-size: 0.7rem;
            padding: 10px 12px;
        }
        
        .glass-container, .stats-container {
            padding: 0.75rem;
        }
        
        .welcome-card, .feature-card {
            padding: 1rem;
        }
    }
    
    /* Animation delays for staggered effects */
    .stats-container:nth-child(1) { animation-delay: 0.1s; }
    .stats-container:nth-child(2) { animation-delay: 0.2s; }
    .stats-container:nth-child(3) { animation-delay: 0.3s; }
    .feature-card:nth-child(odd) { animation-delay: 0.1s; }
    .feature-card:nth-child(even) { animation-delay: 0.2s; }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8, #6a4190);
    }
    
    /* Loading spinner */
    .stSpinner {
        color: white !important;
    }
    
    /* Error message styling */
    .stAlert {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Developer info with social links - moved to top for mobile
st.markdown("""
<div class="developer-info">
    <div style="text-align: center;">
        <strong>👨‍💻 Developed by Deepak Singh</strong>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/deepaksinghai" target="_blank" class="social-link">
                💼 LinkedIn
            </a>
            <a href="https://github.com/CodeWithDks" target="_blank" class="social-link">
                🐙 GitHub
            </a>
            <a href="https://relaxed-trifle-359674.netlify.app" target="_blank" class="social-link">
                🌐 Portfolio
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🧠 Sona</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your Intelligent Educational Assistant</p>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.header("🛠️ Configuration")
    
    # Model settings
    st.subheader("🎯 Model Settings")
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1, 
                           help="Controls creativity in responses. Higher values = more creative, lower = more focused")
    
    # Chat settings
    st.subheader("💬 Chat Settings")
    max_messages = st.number_input("Max Messages to Keep", 10, 100, 50,
                                  help="Maximum number of messages to maintain in chat history")
    
    # Quick actions
    st.subheader("⚡ Quick Actions")
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.messages = [SystemMessage("""You are Sona, an intelligent educational AI assistant designed to help students learn and grow. 
        You are friendly, encouraging, and knowledgeable across various subjects including:
        - Mathematics and Science
        - Literature and Writing
        - History and Social Studies
        - Technology and Programming
        - Study techniques and learning strategies
        
        Always provide clear explanations, use examples when helpful, and encourage critical thinking. 
        Be supportive and motivating while maintaining academic rigor.""")]
        st.rerun()
    
    if st.button("🎯 Reset to Default", type="secondary"):
        st.session_state.messages = [SystemMessage("""You are Sona, an intelligent educational AI assistant designed to help students learn and grow. 
        You are friendly, encouraging, and knowledgeable across various subjects including:
        - Mathematics and Science
        - Literature and Writing
        - History and Social Studies
        - Technology and Programming
        - Study techniques and learning strategies
        
        Always provide clear explanations, use examples when helpful, and encourage critical thinking. 
        Be supportive and motivating while maintaining academic rigor.""")]
        st.rerun()
    
    # Study modes
    st.subheader("📚 Study Modes")
    study_mode = st.selectbox("Choose Study Mode", [
        "General Learning",
        "Exam Preparation",
        "Homework Help",
        "Concept Explanation",
        "Problem Solving"
    ])
    
    st.markdown('</div>', unsafe_allow_html=True)

# Initialize chat history with enhanced system message
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage("""You are Sona, an intelligent educational AI assistant designed to help students learn and grow. 
        You are friendly, encouraging, and knowledgeable across various subjects including:
        - Mathematics and Science
        - Literature and Writing
        - History and Social Studies
        - Technology and Programming
        - Study techniques and learning strategies
        
        Always provide clear explanations, use examples when helpful, and encourage critical thinking. 
        Be supportive and motivating while maintaining academic rigor.""")
    ]

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False

# Statistics section - responsive grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("💬 Messages", len([m for m in st.session_state.messages if isinstance(m, (HumanMessage, AIMessage))]))
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("🤖 AI Responses", len([m for m in st.session_state.messages if isinstance(m, AIMessage)]))
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    st.metric("🌡️ Temperature", f"{temperature}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Welcome message with features
if not st.session_state.chat_started:
    st.markdown("""
    <div class="welcome-card">
        <h2>🎓 Welcome to Sona - Your Educational AI Assistant!</h2>
        <p>I'm here to help you learn, understand, and excel in your studies. Ask me anything!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards - responsive grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📖 Study Help</h3>
            <p>Get explanations for complex topics, homework assistance, and study strategies</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🧮 Problem Solving</h3>
            <p>Step-by-step solutions for math, science, and programming problems</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📝 Writing Support</h3>
            <p>Help with essays, reports, creative writing, and grammar</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Exam Prep</h3>
            <p>Practice questions, review materials, and exam strategies</p>
        </div>
        """, unsafe_allow_html=True)

# Chat container
chat_container = st.container()

with chat_container:
    # Display chat messages from history
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user", avatar="👨‍🎓"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="🧠"):
                st.markdown(message.content)

# Chat input
prompt = st.chat_input("Ask me anything about your studies, homework, or learning...", key="chat_input")

# Static message responses
def get_static_response(user_input):
    """Return static responses for common greetings and farewells"""
    user_input_lower = user_input.lower().strip()
    
    # Greeting messages
    greetings = ["hi", "hello", "hey", "hiya", "sup", "what's up", "good morning", "good afternoon", "good evening"]
    if any(greeting in user_input_lower for greeting in greetings):
        return """🌟 Hello there! I'm Sona, your educational AI assistant! 

I'm here to help you with:
📚 **Study Support** - Explanations, concepts, and learning strategies
🧮 **Problem Solving** - Step-by-step solutions for math, science, and more
📝 **Writing Help** - Essays, reports, grammar, and creative writing
🎯 **Exam Preparation** - Practice questions and study tips
💡 **General Learning** - Any topic you're curious about!

What would you like to learn about today? Feel free to ask me anything! 😊"""
    
    # Farewell messages
    farewells = ["bye", "goodbye", "see you", "farewell", "take care", "later", "catch you later", "see ya"]
    if any(farewell in user_input_lower for farewell in farewells):
        return """👋 Goodbye! It was great helping you learn today! 

Remember:
🌟 Keep curious and keep learning!
📚 Don't hesitate to come back whenever you need help
💪 You've got this - believe in yourself!
🎓 Every question is a step toward knowledge!

Take care, and happy studying! See you next time! 😊✨"""
    
    # Thank you messages
    thanks = ["thank you", "thanks", "thx", "appreciate", "grateful"]
    if any(thank in user_input_lower for thank in thanks):
        return """🙏 You're very welcome! I'm so glad I could help you! 

It makes me happy to be part of your learning journey! 🌟

Remember:
✨ There's no such thing as a silly question
📚 Every bit of learning counts
💡 You're doing great by seeking knowledge!

Feel free to ask me anything else - I'm always here to help! 😊"""
    
    return None

# Handle user input
if prompt:
    st.session_state.chat_started = True
    
    # Add user message to chat
    with st.chat_message("user", avatar="👨‍🎓"):
        st.markdown(prompt)
    
    # Check for static responses first
    static_response = get_static_response(prompt)
    
    if static_response:
        # Display static response with typing effect
        with st.chat_message("assistant", avatar="🧠"):
            # This is the missing code that should be added after line where it cuts off in paste.txt
# Continue from: "with st.chat_message("assistant", avatar="🧠"):"
#                "message_placeholder"

            message_placeholder = st.empty()
            full_response = ""
            
            # Simulate typing effect for static response
            for chunk in static_response.split():
                full_response += chunk + " "
                message_placeholder.markdown(full_response + "▌")
                time.sleep(0.03)
            
            message_placeholder.markdown(full_response)
            
            # Add to session state
            st.session_state.messages.append(HumanMessage(prompt))
            st.session_state.messages.append(AIMessage(static_response))
    else:
        # Modify the prompt based on study mode for AI processing
        enhanced_prompt = f"[Study Mode: {study_mode}] {prompt}"
        st.session_state.messages.append(HumanMessage(enhanced_prompt))
        
        # Generate AI response
        with st.chat_message("assistant", avatar="🧠"):
            with st.spinner("🧠 Thinking..."):
                try:
                    # Initialize the model with current temperature
                    llm = ChatGroq(
                        api_key=st.secrets["GROQ_API_KEY"],
                        model="llama3-8b-8192",
                        temperature=temperature
                    )
                    
                    # Get response
                    result = llm.invoke(st.session_state.messages).content
                    
                    # Display response with typing effect
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    # Simulate typing effect
                    for chunk in result.split():
                        full_response += chunk + " "
                        message_placeholder.markdown(full_response + "▌")
                        time.sleep(0.05)
                    
                    message_placeholder.markdown(full_response)
                    
                    # Add AI response to session state
                    st.session_state.messages.append(AIMessage(result))
                    
                except Exception as e:
                    # Enhanced error handling with helpful static messages
                    error_message = """🚨 **Oops! Something went wrong**

Don't worry, this happens sometimes! Here are a few things you can try:

🔧 **Quick Fixes:**
- Check your internet connection
- Verify your Groq API key is set correctly
- Try refreshing the page
- Wait a moment and try again

💡 **Common Issues:**
- **Timeout**: The AI might be busy - please try again in a moment
- **API Limit**: You might have reached your API usage limit
- **Connection**: Check your internet connection

📚 **In the meantime:**
- Try rephrasing your question
- Break complex questions into smaller parts
- Use the sidebar to adjust settings

I'm here to help once the connection is restored! 😊"""
                    
                    st.error("❌ Technical Issue Detected")
                    
                    # Display friendly error message with typing effect
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    for chunk in error_message.split():
                        full_response += chunk + " "
                        message_placeholder.markdown(full_response + "▌")
                        time.sleep(0.03)
                    
                    message_placeholder.markdown(full_response)
                    
                    # Add error response to session state
                    st.session_state.messages.append(AIMessage(error_message))
    
    # Manage message history length
    if len(st.session_state.messages) > max_messages:
        # Keep system message and trim older messages
        system_msg = st.session_state.messages[0]
        recent_messages = st.session_state.messages[-(max_messages-1):]
        st.session_state.messages = [system_msg] + recent_messages

# Footer
st.markdown("""

""", unsafe_allow_html=True)