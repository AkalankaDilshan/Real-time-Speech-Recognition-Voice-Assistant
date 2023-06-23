import openai

from AI_text_To_voice.text_to_voice import textToSpeech
from main import function_voice_to_text
#from voice_to_text.v2t import voice_to_text_convert

API_KEY = open("API_KEY","r").read()
openai.api_key = API_KEY

chat_log = []

while True:
    another = function_voice_to_text()
    print('user :', another)
    user_message = str(another)
    #user_message = input('user2 : ')
    #user_message =function_voice_to_text()


    if user_message=='exit':
        break
    else:
        chat_log.append({'role':'user','çontent':user_message})

        # response = openai.ChatCompletion.create(
        #     model = "gpt-3.5-turbo",
        #    messages = chat_log)assistant_response
        response = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )


        assistant_response = response['choices'][0]['message']['content']

        print('ChatGPT :',assistant_response)
        textToSpeech(assistant_response)

        