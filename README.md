# 🐉 Dynamic Dragon - An Interactive AI Story Generator

---

## 📝 Project Overview
This project is an interactive website where users can generate stories by making decisions on how they would like the story to go at key points in the narrative. The story evolves dynamically using a free, open-source Large Language Model (LLM) from Ollama.

---

## ✨ Features
- **Dynamic Story Generation:** The story evolves based on user input at key decision points using an advanced LLM.
- **Multiple-Choice Input:** Users make choices that guide the story's direction.
- **Accessibility Feature:** Offer text-to-speech features for the story for those who need it.
- **User-Friendly Interface:** A simple and interactive web design for a smooth user experience.

---

## 💻 Technology Stack
### ⚙️ Backend:
- Python: For handling story logic and integrating the LLM.
- Flask: For hosting the webapp.

### 🎨 Frontend:
- HTML/CSS/JavaScript to build the user interface.

---

## 🔧 Installation and Setup

### ✅ Prerequisites:
- Python 3.8 or above.
- [Ollama app installed from the internet](https://ollama.com/download)

### 📂 Clone the repository:

```sh
git clone https://github.com/TechNerd2009/FBLA_Dynamic_Dragon.git
cd dynamic_dragon
```

### 📦 Install dependencies:

```sh
pip install -r requirements.txt
```

### 📡 Run the backend server:

```sh
flask --app main run
```

---

## 🛠️ How It Works

### 🖱️ User Interaction:

- Users begin the story by clicking on the AI Playground button to start generating.

- At each decision point, multiple-choice options are presented for the user to choose.

- User input is sent to the backend for the AI to process.

### 🧠 Backend Processing:

- The backend appends the user’s choice to the story context.

- The updated context is sent to the LLM, which generates the next part of the story along with new options.

### 🖥️ Frontend Display:

- The generated text is returned to the frontend and displayed to the user.

- The cycle repeats, creating a dynamic storytelling experience.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙏 Acknowledgments

- Ollama for providing access to an open-source LLM.
- [BadgerCMYK](https://www.deviantart.com/badgercmyk/art/Fairytale-Dragon-in-the-Ocean-1057585987) for artwork

---

**💫 Thank you for exploring Dynamic Dragon! We hope you enjoy creating unique and dynamic stories.**
