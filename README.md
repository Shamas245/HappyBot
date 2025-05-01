# Safe AI Mentor

**Smart, Safe & Supportive Learning for All Ages**


---

## 🌟 Overview

The **Child-Safe AI Mentor** is a secure, educational AI platform crafted for children, teens, and adults. It ensures responsible AI usage by offering age-specific interactions, content filtering, and parental control features. Built with Streamlit (frontend), FastAPI (backend), and file-based logs for flagged content, this system prioritizes safety, learning, and engagement.

---

## 🧠 Key Features

### 👥 User Roles
- **Child**: Simple, safe responses with strong filters.
- **Teen**: Balanced AI engagement with educational focus.
- **Mature**: Full access to mentor features.

### ⚠️ Flagging System
- **Automatic**: AI responses are screened and flagged.
- **Manual**: Users can flag questionable content.

### 👨‍👩‍👧 Parent Review Panel
- Review flagged responses
- Approve, delete, or clear all

### 🏆 Positive Badge System
- Encourages good behavior and consistent learning.

### 🎨 Customization
- Avatars, themes, and tone adjustment per user preference.

---

## 📊 System Architecture

```
Frontend (Streamlit) <--> AI Chatbot
     |
  Log File (Flagged Responses)
```

---

## 🚀 How to Run Locally

### Requirements
- Python 3.8+
- Streamlit
- Grok API
- Uvicorn

### Installation
```bash
git clone https://github.com/yourusername/child-safe-ai-mentor.git
cd child-safe-ai-mentor
pip install -r requirements.txt
```

### Run the App
**Backend:**
```bash
uvicorn backend.main:app --reload
```

**Frontend:**
```bash
streamlit run frontend/app.py
```

---

## 📂 Project Structure
```
child-safe-ai-mentor/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── logs/
│   └── flagged_responses.log
├── assets/
│   └── team_members.png
├── README.md
└── requirements.txt
```

---

## 📈 Future Scope
- Sentiment-based moderation
- API integration with third-party filters
- Multilingual support
- Gamification of learning for engagement

---

## 🧡 Meet the Team
This project was collaboratively built by a passionate and talented group:

- **Shamas Liaqat**   
- **Zunaira Hawwar**
- **Muhammad Sajjad**  
- **Majid Ali**  
- **Piotr Karmelita**  
- **Hifza Younas**  

Each member contributed significantly across development, research, design, and testing to ensure the system is safe, functional, and educational.

---

## 🎓 Acknowledgement
Special thanks to the hackathon organizers and community for the opportunity to innovate on AI safety for youth and families.

---

## 📧 Contact
**Team Lead**: Shamas Liaqat  
**Email**: shamasliaqat245@gmail.com  
**GitHub**: [Shamas245](https://github.com/shamas245)

---

## 🔖 License
MIT License. See `LICENSE` for more info.
