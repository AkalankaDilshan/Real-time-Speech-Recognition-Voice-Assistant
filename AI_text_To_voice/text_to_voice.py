import pyttsx3


def textToSpeech(answer):

    text_to_speech = pyttsx3.init()

    #changing voice
    voices = text_to_speech.getProperty('voices')
    text_to_speech.setProperty('voice', voices[1].id)

    #changing speech rate
    rate = text_to_speech.getProperty('rate')
    text_to_speech.setProperty('rate', rate - 60)

    #Changing volume
    volume = text_to_speech.getProperty('volume')
    text_to_speech.setProperty('volume',volume - 0.25)

    #speech
    text_to_speech.say(answer)
    text_to_speech.runAndWait()

#textToSpeech("The Mission of the Faculty of Science of the University of Kelaniya is to produce highly motivated graduates and postgraduates capable of making a significant contribution towards national development and the well being of mankind, to conduct research and provide advice and consultancy services in various scientific disciplines to foster a better understanding of the environment for sustainable use and conservation of natural resources.")