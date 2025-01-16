# **FBLA Introduction to Programming Prompt**
Write an interactive story that occasionally asks the user what they’d like to do, and changes
where the story goes based on user input. Allow the user to stop interacting with the story by
saying “stop.”

# **Project Overview**
This project is an interactive website where users can generate stories by making decisions on how they would like the story to go at key points in the narrative. The story evolves dynamically using a free, open-source Large Language Model (LLM), called Ollama.

# **Features**
- **Dynamic Story Generation:** The story evolves based on user input at key decision points using an advanced LLM.
- **Multiple-Choice Input:** Users make choices that guide the story's direction.
- **Accessibility Feature:** Offer text-to-speech features for the story for those who need it.
- **User-Friendly Interface:** A simple and interactive web design for smooth user experience.

# **Technology Stack**
**Backend:**
- Python: For handling story logic and integrating the LLM.
- Flask: For hosting the webapp.

**Frontend:**
- HTML/CSS/JavaScript to build the user interface.

# **Installation and Setup**

**Prerequisites:**
- Python 3.8 or above.
- [Ollama app installed from internet](https://ollama.com/download)

**Clone the repository:**

`git clone {url}`</br>
`cd {name}`

**Install dependencies:**

`pip install -r requirements.txt`

**Run the backend server:**

`flask --app main run`


# **How It Works**

**User Interaction:**

- Users begin the story by clicking on the AI Playground button to start generating.

- At each decision point, multiple-choice options are presented for the user to choose.

- User input is sent to the backend for the AI to process.


**Backend Processing:**

- The backend appends the user’s choice to the story context.

- The updated context is sent to the LLM, which generates the next part of the story along with new options.

**Frontend Display:**

- The generated text is returned to the frontend and displayed to the user.

- The cycle repeats, creating a dynamic storytelling experience.


# **License**

This project is licensed under the MIT License. See the LICENSE file for details.

# **Acknowledgments**

- Ollama for providing access to an open-source LLM.
- [BadgerCMYK](https://www.deviantart.com/badgercmyk/art/Fairytale-Dragon-in-the-Ocean-1057585987) for artwork

Thank you for exploring Dynamic Dragon! We hope you enjoy creating unique and dynamic stories.



