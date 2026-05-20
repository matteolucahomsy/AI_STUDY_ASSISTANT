# 🧠 AI Study Assistant

A simple full-stack AI Study Assistant built with:

- ⚛️ React (Frontend)
- ⚡ FastAPI (Backend)
- 🔗 REST API communication

---

## 🚀 Features

- Connects React frontend to FastAPI backend
- Simple API endpoint `/chat`
- Displays AI response in UI
- CORS enabled for frontend communication

---

## 📁 Project Structure
frontend/ -> React app
backend/ -> FastAPI server


---

## ⚙️ Backend Setup (FastAPI)

### Install dependencies
```bash
pip install fastapi uvicorn flask-cors
```
Run server
```bash 
uvicorn main:app --reload
```

Backend runs on:
http://217.0.0.1:8000

## 💻 Frontend Setup (React)
### Install dependencies
```bash
nom install
```
Run app 
```bash
nom run dev
```
Frontend runs on:
http://localhost:5175/

## 🔗 API Endpoint

| Method | Endpoint | Description              |
| ------ | -------- | ------------------------ |
| GET    | `/chat`  | Returns a simple message |

## 🛠 Future Improvements
- Add real AI integration (OpenAI / LLM)
- Add chat input box
- Save conversation history
- Deploy backend + frontend

## 👨‍💻 Author
MATTEO LUCA HOMSY
