import gtts
import os
import time


def clear(path = 'assets/speech/ai.mp3'):
    if os.path.exists(os.path.join(os.getcwd(), path)):
        os.remove(os.path.join(os.getcwd(), path))
        print('pulito')
        
def text_to_speech(text):
    clear()
    lang = 'it'
    output = 'assets/speech/ai.mp3'
    speech = gtts.gTTS(text=text, lang=lang, slow=False, tld='it')
    speech.save('assets/speech/ai.mp3')
    return '/speech/ai.mp3'
    
    
# text_to_speech('come va')