# AI Language Tutor

## 📌 Project Overview
AI Language Tutor is an innovative language learning platform developed for **HACK O OCTO 2.0** 🚀. This AI-powered language learning assistant leverages **Azure Translator API** for real-time translation, pronunciation feedback, and interactive learning experiences. Built with **Streamlit** and powered by **Azure AI services**, this application offers a comprehensive language learning solution.

## 🚀 Features
- **Real-time Translation** – Instant translation using Azure Translator API
- **Intelligent AI Tutor** – Experience natural, context-aware conversations
- **Pronunciation Feedback** – Get instant feedback on your pronunciation
- **Customized Learning Paths** – Personalized lesson plans based on your goals
- **Vocabulary Builder** – Smart vocabulary tracking and practice system
- **Interactive Quizzes** – Dynamic assessment tools for learning reinforcement
- **Progress Analytics** – Comprehensive learning history and progress tracking

## 🏗️ Tech Stack
- **Frontend:** Streamlit (Modern UI framework)
- **Backend:** 
  - Azure Translator API (Real-time translation)
  - Azure AI Services (Advanced language processing)
  - Azure Speech Services (Pronunciation feedback)
- **Data Management:** Secure JSON storage (User profiles, learning data)
- **UI/UX:** Custom CSS/HTML for enhanced visual appeal

## 📂 Project Structure
```plaintext
AI_LANGUAGE_TUTOR/
│── assets/                # Data storage
│   │── chat_history.json      # Conversation records
│   │── lesson_plan_inputs.json  # Learning preferences
│   │── lesson_plan.json        # Customized lesson plans
│   │── user_vocabulary.json    # Personal vocabulary database
│
│── pages/                # Application pages
│   │── chatbot.py         # AI interaction interface
│   │── history.py         # Learning progress tracker
│   │── lesson_plan.py     # Lesson management
│   │── vocab.py           # Vocabulary tools
│
│── utils/                 # Core utilities
│   │── config.json        # System configuration
│   │── storage.py         # Data management
│   │── translator.py      # Azure Translator API integration
│   │── speech.py          # Azure Speech Services integration
│
│── .gitignore             # Version control settings
│── app.py                 # Application entry point
│── sidebar.py             # Navigation component
│── README.md              # Project documentation
```

## 🛠️ Setup & Installation
### **Configuration**
- Access settings in `utils/config.json`
- Configure Azure services:
  - Azure Translator API credentials
  - Azure Speech Services credentials
  - Azure AI service parameters
- Set your preferred learning language
- Add your Azure credentials securely

### **Requirements**
- **Python 3.8+** environment
- Azure services subscription:
  - Azure Translator API
  - Azure Speech Services
  - Azure AI Services
- Modern web browser

### **Installation**
1. **Clone Repository:**
   ```sh
   git clone https://github.com/your-repo/AI-Language-Tutor.git
   cd AI-Language-Tutor
   ```
2. **Environment Setup:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Launch Application:**
   ```sh
   streamlit run app.py
   ```

## 📖 User Guide
1. **Launch** the application and choose your learning activity
2. **Practice** with real-time translation and pronunciation feedback
3. **Interact** with the AI tutor for personalized practice
4. **Generate** custom lesson plans aligned with your goals
5. **Build** your vocabulary through the smart tracking system
6. **Test** your knowledge with interactive quizzes
7. **Monitor** your progress through detailed analytics

## 🎯 Future Roadmap
- 🔄 Enhanced speech recognition with more languages
- 🔄 Advanced pronunciation scoring system
- 🔄 Real-time conversation practice
- 🔄 Multi-language support expansion
- 🔄 Offline learning capabilities
- 🔄 Mobile app version

## 👨‍💻 Developers
**Abhay Gupta & Kripanshu Gupta**  
Developed for HACK O OCTO 2.0 🚀  
Connect with us on [LinkedIn](https://www.linkedin.com/) to learn more about our work!

---
🔹 *AI Language Tutor - Empowering Language Learning Through Innovation*

## 📹 Demo
Check out our demo video: [Azure AI Output_video.mp4](Azure%20AI%20Output_video.mp4)

