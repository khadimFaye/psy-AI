import flet as ft
import gtts, time
import speech_recognition as sr
from plyer import audio

import wavio as wv

import os


#Recognizer.record()
#Recognizer.recognize_google_cloud()


#def Registra_Audio(duration:int = 5, freq:int = 44100):
#    audio = sd.rec(
#        int(duration *freq),
#        samplerate=freq,
#        channels=2
#    )
#    sd.wait()
#    return audio
#
#
#def save_audio(NumPArray, rate):
#    path = os.path.join(os.getcwd(), 'campione.wav')
#    wv.write(file=path, data=NumPArray, rate=44100, sampwidth=2)
#    print('salvato')

def audio_trascrizione(*args):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source=source)
        audio_data = recognizer.listen(source=source)

    text = recognizer.recognize_sphinx(audio_data) 
    print(text)
    



def talk(*arg):
    pass
    
   

class Chat(ft.Column):
    __audio = audio
    def __init__(self, page, back=None, *args):
        self.page = page
        self.back = back

        self.Chat_column = ft.Column(height=700, scroll=ft.ScrollMode.ALWAYS, auto_scroll=True)

        self.textinput = ft.TextField(
            border_color=ft.colors.PURPLE_500, border=10,
            border_radius=12,
            bgcolor=ft.colors.WHITE,
            hint_text='esprimiti...',
            hint_style=ft.TextStyle(color='black'),
            text_style=ft.TextStyle(color='black'),
            expand=True,
            on_change=self.switch_text_mode
            
        )

        self.record_button = ft.IconButton(icon=ft.icons.RECORD_VOICE_OVER_ROUNDED, icon_color='black', on_click=self.Registra_audio)
        self.stop_record_button = ft.IconButton(icon=ft.icons.PAUSE_CIRCLE_OUTLINE_OUTLINED, icon_color='black', on_click=self.Registra_audio)
        self.sumbitButton = ft.IconButton(icon=ft.icons.SEND_ROUNDED, icon_color='black', on_click=self.sumbit)

        self.buttonContainer =  ft.CircleAvatar(
                                bgcolor='white',
                                content=self.record_button
                                    )
        super().__init__(
            expand=True,
            controls = [
                ft.Container(padding = 10, content=ft.Row(controls=[ft.Row(alignment=ft.MainAxisAlignment.START, controls = [ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, icon_color='white', on_click=self.back, icon_size=20)]), ft.Row(expand=True, alignment=ft.MainAxisAlignment.CENTER, controls = [ft.Text(value='PsyAI', size=40, weight='bold', )])])),
                ft.Container(padding = 10, content=ft.Column(
                    controls=[
                        self.Chat_column,

                        ft.Column(expand = True, horizontal_alignment=ft.CrossAxisAlignment.END, controls=[

                            ft.Row(controls=[
                                self.textinput, 
                                self.buttonContainer
                                    
                                    ])
                        ])

                    ]
                ))
            ],

            
        )
    def sendMessage(self, args):
        pass

    def Registra_audio(self, e):
        if e.control.icon ==ft.icons.RECORD_VOICE_OVER_ROUNDED:
            self.buttonContainer.content = self.stop_record_button
            self.buttonContainer.update()
            self.update()
            audio_trascrizione()
          
     

        elif e.control.icon ==ft.icons.PAUSE_CIRCLE_OUTLINE_OUTLINED:
            self.buttonContainer.content = self.record_button
            self.buttonContainer.update()
            self.update()
            self.__audio.stop()
            print(self.__audio.file_path)
    def sumbit(self, *args):
        self.Chat_column.controls.append(
            ft.Row(
                controls=[
                    ft.Container(
                        expand = True,
                        content=ft.Text(expand=True, value=self.textinput.value, size = 15, weight=ft.FontWeight.NORMAL, color='black', text_align=ft.TextAlign.RIGHT),
                        bgcolor = 'white' ,
                        border_radius = ft.border_radius.only(bottom_right=12, bottom_left=12, top_right=12),
                        padding = 10
                                 )
                    
                    ])
        )
        self.Chat_column.update()
        self.update()

    def switch_text_mode(self, *args):
        if self.buttonContainer.content!= self.sumbitButton:
            self.buttonContainer.content = self.sumbitButton
            self.buttonContainer.update()
            self.update()
  



class Home(ft.Column):
  
    def __init__(self, page, *args):
        super().__init__(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[

                ft.Container(height = 200),
                ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=[
                    ft.Row(controls=[ft.Text(value ='Psy-AI', color='white', size=30, weight='bold')], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[ft.Text(expand = True,value ='Chatta con il tuo AI psycologo in tutta confidenza e senza giudizio!', color='white', size=12, weight='w500', text_align=ft.TextAlign.CENTER)], alignment=ft.MainAxisAlignment.CENTER)
                ]),
            ft.Container(height = 10),
            ft.Row(controls=[
                ft.Container(
                    padding = 5, 
                    content = ft.ElevatedButton(
                        height=60, 
                        expand = True, 
                        on_click = self.start_session,
                        content =ft.Text(value = 'avvia seduta!', color='white',size=18, weight='w800'), bgcolor=ft.colors.PURPLE_500,))], alignment=ft.MainAxisAlignment.CENTER,)
            ],


            
        )
    def start_session(self, *args):
        for child in self.controls:
            child.visible = False
            child.update()
        self.controls.append(Chat(self.page, back=self.back))
        self.update()

    def back(self, *args):
        self.controls.pop()
        for child in self.controls:
            child.visible = True
            child.update()
        self.update()

    
        

def main(page:ft.Page):
    page.title = 'Psco AI'
    page.window.height, page.window.width = (640, 340)

    page.add(ft.Container(padding = 10, content=ft.SafeArea(Home(page))))
    page.bgcolor = ft.colors.ORANGE_800
    page.update()


if __name__=='__main__':
    ft.app(target=main, view = ft.AppView.WEB_BROWSER)
