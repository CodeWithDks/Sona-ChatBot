# 🧠 Sona - Educational AI Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=groq&logoColor=white" alt="Groq">
</div>

<div align="center">
  <h3>🎓 Your Intelligent Educational Companion</h3>
  <p>A modern, interactive AI assistant designed to help students learn, understand, and excel in their studies.</p>
</div>

---

## 🌟 Features

### 🎨 **Modern Design**
- **Animated gradient background** with smooth color transitions
- **Glassmorphism UI** with blur effects and transparency
- **Floating animations** and hover effects
- **Responsive design** that works on all devices
- **Dark theme** with vibrant accents

### 🧠 **Educational Capabilities**
- **Multi-subject support**: Mathematics, Science, Literature, History, Programming
- **Study modes**: General Learning, Exam Preparation, Homework Help, Concept Explanation
- **Interactive learning**: Step-by-step problem solving
- **Writing assistance**: Essays, reports, grammar help
- **Exam preparation**: Practice questions and study strategies

### 💬 **Smart Interactions**
- **Static responses** for greetings, farewells, and thanks
- **Context-aware** conversations with chat history
- **Typing animation** for realistic chat experience
- **Error handling** with helpful troubleshooting messages
- **Temperature control** for response creativity

### ⚡ **Performance Features**
- **Fast response times** with Groq API
- **Message history management** with configurable limits
- **Real-time statistics** tracking
- **Optimized UI** with smooth animations

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/sona-ai-assistant.git
   cd sona-ai-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8501`

---

## 📦 Dependencies

```txt
streamlit>=1.28.0
langchain-groq>=0.1.0
langchain-core>=0.2.0
python-dotenv>=1.0.0
```

---

## 🎯 Usage

### Basic Interaction
Simply type your questions or learning needs in the chat input. Sona can help with:

- **Homework questions**: "Explain photosynthesis"
- **Math problems**: "Solve this quadratic equation: x² + 5x + 6 = 0"
- **Writing help**: "Help me improve this essay introduction"
- **Study strategies**: "How should I prepare for my history exam?"

### Study Modes
Select from different study modes in the sidebar:
- **General Learning**: Broad educational support
- **Exam Preparation**: Focused exam prep assistance
- **Homework Help**: Specific assignment support
- **Concept Explanation**: Deep dive into topics
- **Problem Solving**: Step-by-step solutions

### Settings
Customize your experience:
- **Temperature**: Control response creativity (0.0-2.0)
- **Message History**: Set maximum chat history length
- **Quick Actions**: Clear chat or reset to defaults

---

## 🛠️ Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for AI responses | Yes |

### Streamlit Configuration
The app uses these Streamlit settings:
- **Page Title**: "Sona - Educational AI Assistant"
- **Page Icon**: 🧠
- **Layout**: Wide
- **Sidebar**: Expanded by default

---

## 🎨 Design Philosophy

### Visual Design
- **Glassmorphism**: Modern frosted glass effect
- **Animated Gradients**: Dynamic color-shifting backgrounds
- **Micro-interactions**: Subtle animations for better UX
- **Accessibility**: High contrast and readable typography

### User Experience
- **Immediate Feedback**: Instant responses for common greetings
- **Error Recovery**: Helpful messages when things go wrong
- **Progressive Disclosure**: Features revealed as needed
- **Consistent Branding**: Cohesive visual identity throughout

---

## 📊 Technical Architecture

### Core Components
```
sona-ai-assistant/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── README.md            # This file
└── assets/              # Static assets (if any)
```

### Data Flow
1. **User Input** → Streamlit chat interface
2. **Static Check** → Predefined responses for common messages
3. **AI Processing** → Groq API via LangChain
4. **Response Display** → Animated typing effect
5. **History Management** → Session state storage

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Groq** for providing fast AI inference
- **LangChain** for excellent AI framework
- **Streamlit** for the amazing web framework
- **Inter Font** for beautiful typography

---

## 📞 Support

Having issues? Here are some resources:

### Common Issues
- **API Key Issues**: Ensure your Groq API key is set correctly
- **Connection Problems**: Check your internet connection
- **Performance**: Try adjusting the temperature or message history settings

### Get Help
- 📧 **Email**: support@your-domain.com
- 💬 **Discord**: Join our community server
- 📝 **Issues**: Open a GitHub issue

---

## 👨‍💻 Developer

**Deepak Singh**
- 💼 [LinkedIn](https://linkedin.com/in/deepak-singh)
- 🐙 [GitHub](https://github.com/deepak-singh)
- 🌐 [Portfolio](https://deepak-portfolio.com)

---

<div align="center">
  <p>Made with ❤️ for education</p>
  <p>🌟 <strong>Empowering students to learn, grow, and succeed</strong> 🌟</p>
</div>

---

## 🔮 Future Enhancements

- [ ] **Voice Integration**: Voice input/output capabilities
- [ ] **File Upload**: Support for document analysis
- [ ] **Study Planner**: AI-powered study schedule creation
- [ ] **Progress Tracking**: Learning analytics and insights
- [ ] **Collaborative Features**: Group study sessions
- [ ] **Mobile App**: Native mobile application
- [ ] **Offline Mode**: Basic functionality without internet
- [ ] **Multi-language**: Support for multiple languages

---

*Last updated: July 2025*