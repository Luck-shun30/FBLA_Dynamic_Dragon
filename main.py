from flask import Flask, render_template, request, redirect, url_for

from ollama import chat
from ollama import ChatResponse

#options aren't shown in the ai request so resulting story is random. add global var for the options available and add that to prompt.
active_story = ""
choice = ""
options = []
option_a = ""
option_b = ""
option_c = ""

def llmgenerate():
   SYSTEM_PROMPT = 'Continue the fantasy story without adding anything else. Do not end the story.'
   global choice
   global active_story
   global options
   global option_a
   global option_b
   global option_c
   print(choice)
   response = ChatResponse = chat(model='llama3.2', messages=[
   {
      'role': 'user',                                                                                                               #TODO: Options cause it to give new options instead of reading them. Take the list of options out so that only the chosen choice is listed for it to continue.
      'content': "System Prompt:" + SYSTEM_PROMPT + "\nConversation history/Story that you need to continue: " + active_story + "\nChosen option (how the story should go): " + choice + "\nContinue the story by adding on to it based on the chosen option (return the new story as an addition)."
   }
   ])

   active_story += "\n" + response.message.content

   return active_story

def options_generate():
   OPTIONS_SYSTEM_PROMPT = "Return 3 short options to continue the story without adding anything else before or after the options. Do not end the story. Here's an example: 'A) Do this. B) Do that C) Do that'. Use third-person perspective and present tense. Be vague in the options."
   global choice
   global active_story

   options = ChatResponse = chat(model='llama3.2', messages=[
   {
      'role': 'user',
      'content': "System Prompt:" + OPTIONS_SYSTEM_PROMPT + "\nConversation history / Story that you need to give options for: " + active_story + "<br>"
   }
   ])

   options = options.message.content

   option_a = options[0:options.find("B)")]
   options = options.replace(option_a, '')

   option_b = options[0:options.find("C)")]
   options = options.replace(option_b, '')

   option_c = options

   options = [option_a, option_b, option_c]
   
   return options
 
# Create the Flask instance and pass the Flask 
# constructor the path of the correct module
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('./index.html')

@app.route('/load')
def load():
   return render_template('./loading.html')
 
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    global choice
    if request.method == 'POST':
        choice = request.form.get('options')
        if choice == "Exit":
            return redirect(url_for('/'))  # Redirect to an / route
    story = llmgenerate()
    options = options_generate()
    return render_template('answer.html', 
                           text=story, option_a=options[0], option_b=options[1], option_c=options[2])

 
 
# Start with flask web app with debug as
# True only if this is the starting page
if(__name__ == "__main__"):
    app.run(debug=True)