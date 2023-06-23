import speech_recognition as sr


def function_voice_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        #print("Please say something")

        audio = r.listen(source)

        #print("Recognizing Now .... ")

        # recognize speech using google

        try:
            return r.recognize_google(audio)
            #print("You have said : " + r.recognize_google(audio))
            #print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))

        # write audio
        # with open("recorded.wav", "wb") as f:
        #     f.write(audio.get_wav_data())


if __name__ == "__main__":
    function_voice_to_text()

# import speech_recognition as sr
#
# def recognize_speech_from_mic(recognizer, microphone):
#
#     print('user : ')
#     if not isinstance(recognizer, sr.Recognizer):
#         raise TypeError("`recognizer` must be `Recognizer` instance")
#
#     if not isinstance(microphone, sr.Microphone):
#         raise TypeError("`microphone` must be `Microphone` instance")
#
#     # adjust the recognizer sensitivity to ambient noise and record audio
#     # from the microphone
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#
#     # set up the response object
#
#     response = {
#         # "success": True,
#         # "error": None,
#          "transcription": 2
#     }
#
#     # try recognizing the speech in the recording
#     # if a RequestError or UnknownValueError exception is caught,
#     #     update the response object accordingly
#     try:
#         response["transcription"] = recognizer.recognize_google(audio)
#     except sr.RequestError:
#         # API was unreachable or unresponsive
#         response["success"] = False
#         response["error"] = "API unavailable"
#     except sr.UnknownValueError:
#         # speech was unintelligible
#         response["error"] = "Unable to recognize speech"
#
#     return response['transcription']
#
# def function_voice_to_text():
#     # create recognizer and mic instances
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()
#     guess = recognize_speech_from_mic(recognizer, microphone)
#     return print(guess)
#
# if __name__ == "__main__":
#     function_voice_to_text()





