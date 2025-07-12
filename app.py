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

# Custom CSS for modern styling with animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated gradient background */
    .main-container {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        min-height: 100vh;
        position: relative;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Pulse animation */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Glow effect */
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.3); }
        50% { box-shadow: 0 0 30px rgba(102, 126, 234, 0.6); }
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        animation: float 3s ease-in-out infinite;
    }
    
    .sub-header {
        text-align: center;
        color: #64748b;
        font-size: 1.4rem;
        margin-bottom: 2rem;
        font-weight: 400;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .developer-info {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 15px 20px;
        border-radius: 25px;
        font-size: 0.9rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        z-index: 1000;
        animation: glow 3s ease-in-out infinite;
        transition: all 0.3s ease;
    }
    
    .developer-info:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
    }
    
    .social-links {
        display: flex;
        gap: 10px;
        margin-top: 8px;
        justify-content: center;
    }
    
    .social-link {
        color: white;
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        font-size: 0.8rem;
    }
    
    .social-link:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.1);
        color: white;
        text-decoration: none;
    }
    
    .stats-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        animation: float 2s ease-in-out infinite;
    }
    
    .stats-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }
    
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 1rem;
        margin: 1rem 0;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        animation: float 2.5s ease-in-out infinite;
    }
    
    .welcome-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 25px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
        animation: pulse 3s ease-in-out infinite;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 20px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }
    
    /* Button animations */
    .stButton button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }
    
    /* Slider styling */
    .stSlider {
        padding: 1rem 0;
    }
    
    /* Input styling */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        color: white;
        backdrop-filter: blur(10px);
    }
    
    /* Metrics styling */
    .metric-container {
        text-align: center;
        color: white;
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: white;
    }
    
    /* Animation delays for staggered effects */
    .stats-container:nth-child(1) { animation-delay: 0.1s; }
    .stats-container:nth-child(2) { animation-delay: 0.2s; }
    .stats-container:nth-child(3) { animation-delay: 0.3s; }
</style>
""", unsafe_allow_html=True)

# Apply animated background
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Developer info with social links
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

# Statistics section
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
    
    # Feature cards
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
<div class="footer">
    <h3>🚀 Powered by Advanced AI Technology</h3>
    <p>🧠 Groq & LangChain | 🎨 Built with Streamlit</p>
    <p>💡 Empowering students to learn, grow, and succeed</p>
    <p>🌟 Made with ❤️ for education</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main container