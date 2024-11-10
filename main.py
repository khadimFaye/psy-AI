import flet as ft
# import time
# import speech_recognition as sr
# import  sounddevice as sd
import os
# import numpy as np

# from utils.speech_to_text import recognise as rc
# from model import assistente_psicologo as ap
# from theme.pallet import palette as pt
from utils.views import change_route

font_path = '/fonts/Exo/static/assets/fonts/Exo/static/'

    

def main(page:ft.Page):
    page.title = 'Psy-AI'
    page.window.height, page.window.width = (640, 340)
    page.on_route_change = lambda _ : change_route(page)
    
    # page.bgcolor = 'white'
    # page.bottom_appbar = ft.BottomAppBar(content=ft.TextField(expand=True, multiline=True), )
    page.go('/')
    page.update()

    


if __name__=='__main__':
    ft.app(target=main, view = ft.AppView.WEB_BROWSER, assets_dir='assets')


# SILENCE_DURATION:int = 1
# FREQUENZA:int = 44100 
# CHUNCK = 1024 
# CANALI = 1 
# SOGLIA_SILENZIO = 100
# # FORMAT = pyaudio.paInt16



# __processing :bool =0
# frames = 0

# # def save_audio(data):
# #     wv.write("audio.wav", data, sampwidth=2, rate=FREQUENZA)
# #     # with wave.open('audio.wav', 'wb') as wf:
# #     #     wf.setnchannels(CANALI)
# #     #     wf.setframerate(FREQUENZA)
# #     #     wf.setsampwidth(p.get_sample_size(FORMAT))
# #     #     wf.writeframes(data)
    
   
# # def Registra_Audio():
    
# #     for i in range(10):
        
# #         audio = sd.rec(int(10 * FREQUENZA), samplerate=FREQUENZA, channels=1)
        
# #         audio_data = np.frombuffer(audio)
# #         intensita = np.abs(audio_data).mean()
# #         sd.wait()
        
# #         print(intensita)
# #         # print(audio)
# #         print('registrando....')
# #         print('finit .')
# #         save_audio(audio)
# #         print(audio)
    
#     # return audio
#     # p = pyaudio.PyAudio()
#     # flusso_registrazione = p.open(
#     #     format=FORMAT,
#     #     channels=CANALI,
#     #     rate=FREQUENZA,
#     #     input=True,
#     #     frames_per_buffer=CHUNCK
#     #     )
    
#     # frames = []
#     # tempo_di_silnezio = None
#     # # for _ in range(0, int(FREQUENZA/CHUNCK *10)):
#     # #     dati = flusso_registrazione.read(CHUNCK)
#     # #     frames.append(dati)
        
#     # while True:
#     #     data = flusso_registrazione.read(CHUNCK)
#     #     audio_data = np.frombuffer(buffer=data, dtype=np.int16)
#     #     intensita = np.abs(audio_data).mean()
#     #     print(intensita)
#         # if intensita < SOGLIA_SILENZIO:
#         #     if tempo_di_silnezio is None:
#         #         tempo_di_silnezio = time.time()
#         #     elif time.time() - tempo_di_silnezio > SILENCE_DURATION:
#         #         print('chiuso')
#         #         break
            
#         # else:
#         #     tempo_di_silnezio=None
        
#         #frames.append(data)
            
      
#     # flusso_registrazione.stop_stream()
#     # flusso_registrazione.close()
#     # p.terminate()

#     # print('terminato')
        
#     # save_audio(b''.join(frames), p)
        
    