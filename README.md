**FBLA Intro to Programming Prompt**

Story generating website that continues story based on user chosen choices.
Uses a Flask server to validate user input while using advanced LLM to generate parts of the story.

**LLM**: Ollama

**Server**: Flask

**Text-to-speech Feature**: JS Speech Synthesis

Preview (Coming Soon):

Interactive AI Story Generator

# **Project Overview**
This project is an interactive website where users can collaboratively generate stories by making multiple-choice decisions at key points in the narrative. The story evolves dynamically using a free, open-source Large Language Model (LLM), called Ollama.

# **Features:**
Dynamic Story Generation: The story evolves based on user input at key decision points.
Multiple-Choice Input: Users make choices that guide the story's direction.
AI Integration: Powered by open-source LLMs for natural and coherent story generation.
User-Friendly Interface: A simple and interactive web design for smooth user experience.

# **Technology Stack**
Backend:
Python: For handling story logic and integrating the LLM.
Flask: For hosting the webapp.

Frontend:
HTML/CSS/JavaScript: For building the user interface.

# **Installation and Setup**

Prerequisites:
Python 3.8 or above.
Flask installed in Python environment
[Ollama app installed from internet](https://ollama.com/download)
GPU (optional but recommended for faster model inference).

Clone the repository:

git clone https://github.com/your-username/interactive-ai-story-generator.git
cd interactive-ai-story-generator

Install dependencies:

`pip install -r requirements.txt`

Run the backend server:

`flask --app main run`


# **How It Works**

**User Interaction:**

Users begin the story by choosing an initial prompt.

At each decision point, multiple-choice options are presented.

User input is sent to the backend.


**Backend Processing:**

The backend appends the user’s choice to the story context.

The updated context is sent to the LLM, which generates the next part of the story.

Frontend Display:

The generated text is returned to the frontend and displayed to the user.

The cycle repeats, creating a dynamic storytelling experience.

Customization

Story Themes: Modify the initial prompts and decision points to create themed stories (e.g., fantasy, sci-fi, mystery).

Model Fine-Tuning: Train the model with a custom dataset for specific narrative styles.

User Interface: Customize the frontend for a more immersive experience.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch:

git checkout -b feature-name

Commit your changes:

git commit -m "Add feature description"

Push to the branch:

git push origin feature-name

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Hugging Face for providing access to open-source LLMs.

Open-source contributors and the AI community for their valuable resources.

Thank you for exploring the Interactive AI Story Generator! We hope you enjoy creating unique and dynamic stories.



