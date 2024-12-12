from ollama import chat
from ollama import ChatResponse

#You are an AI storyteller. Start a fantasy story and pause after each paragraph to ask the user what happens next. Do NOT end the story. Make sure the paragraph is short and is under 900 letters. Do NOT immediately finish a story with a conclusion and moral; make short parts of stories that could be continued. Ask them a multiple choice question and list choices at the end of a paragraph to allow the user to continue the story in a way they want. Give them choices and listen to the input choices. Do not fill in any user input by yourself. You must NOT say anything other the story. Make sure the content is appropriate. If there is an active story that is being continued, return the same story along with the 1 paragraph addition.

SYSTEM_PROMPT = 'Continue the fantasy story without adding anything else. Give 3 options based on how the story could go. Do not end the story.'
active_story = ""
choice = ""


while (choice != "end" or choice == ""):
    response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': "System Prompt:" + SYSTEM_PROMPT + "\nStory: " + active_story + "\nChosen option: " + choice + "\nContinue the story by adding on to it (return the new story as an addition)"
    }
    ])
    # or access fields directly from the response object
    print(response.message.content)

    choice = input("Choose an option: (A/B/C): ")

    while (not(choice == "A" or choice == "B" or choice == "C" or choice == "end")):
        choice = input("Choose an option: (A/B/C): ")