import flet as ft
from utils.speech_to_text import recognise as rc
from theme.pallet import palette as pt
from utils.model import assistente_psicologo as ap
from utils.text_speech import text_to_speech as tp
import threading

font_path = '/fonts/Exo/static/assets/fonts/Exo/static/'

class permissionHandler(ft.PermissionHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def check_permission(self, of: ft.PermissionType, wait_timeout: float | None = 25) -> ft.PermissionStatus | None:
        return super().check_permission(of, wait_timeout)
    
    def request_permission(self, of: ft.PermissionType, wait_timeout: float | None = 25) -> ft.PermissionStatus | None:
        return super().request_permission(of, wait_timeout)
    
    def open_app_settings(self, wait_timeout: float | None = 10) -> bool:
        return super().open_app_settings(wait_timeout)
    

class HumanchatWidget(ft.Row):

    def __init__(self, page,text:str = '', bgcolor :any = 'blue400', color = 'white',  role ='Tu',*args, **kwargs):
        self.page = page
        super().__init__(
            
            alignment=ft.MainAxisAlignment.END,
            expand=True,
                
                controls=[
                    ft.Container(
                        expand=True if len(text)>30 else False,
                        # width = width,
                        content=ft.Text(selectable=True, expand=True, value=text, size = 15, weight=ft.FontWeight.NORMAL, color=color, text_align=ft.TextAlign.RIGHT),
                        bgcolor = bgcolor ,
                        padding = 10, 
                        # gradient = ft.LinearGradient(colors=['blue800', 'blue', 'white'], tile_mode=ft.GradientTileMode.CLAMP) if bgcolor is None else None,
                        border_radius = ft.border_radius.only(top_left=15, bottom_left=15, bottom_right=15, top_right=15) ,
                        
                                 ),
                    
                    ft.Container(content=ft.Text(value =role,)),
                    
                    ]
                         )
class AIchatWidget(ft.Row):

    def __init__(self, page,text:str = '', role ='psy-AI',expand = 1, *args, **kwargs):
        self.page = page
        super().__init__(
            
            alignment=ft.MainAxisAlignment.START,
            expand=True,
                
                controls=[
                ft.Container(content=ft.Text(value =role, color=ft.colors.GREY_400)),
                    ft.Container(
                        expand=True if len(text)>40 else False,
                        # width = width,
                        content=ft.Text(selectable=True, expand=True, value=text, size = 15, weight=ft.FontWeight.W_400, color='black87', text_align=ft.TextAlign.LEFT),
                        bgcolor = 'white' ,
                        padding = 10, 
                        # gradient = ft.LinearGradient(colors=['blue800', 'blue', 'white'], tile_mode=ft.GradientTileMode.CLAMP) if bgcolor is None else None,
                        border_radius = ft.border_radius.only(top_right=15, bottom_left=0, bottom_right=15, top_left=15),
                        
                                 ),
                    
                    
                    ]
                         )
    
    
def ciao(*args):
    print('cambiato')
   

class Chat(ft.Column):
    __process_flag = 0
    _first_entry:bool =1
    _output_path: str = 'assets/speech/audio.wav'
    
    header_text = 'Heila ciao! come\'è la giornata?\n'
    header_text2 = 'Chatta con il tuo assistente psicologico AI, '
    label = 'uno spazio sicuro per esprimerti liberamente e '
    label1 = 'trovare conforto senza giudizio.'
    mini_bot = ft.Image(
        src = '/icons/mini-bot.gif',
        filter_quality=ft.FilterQuality.HIGH,
       animate_opacity=ft.Animation(duration=20, curve=ft.AnimationCurve.EASE_IN,), 
        animate_scale=ft.Animation(duration=100, curve=ft.AnimationCurve.BOUNCE_IN_OUT,), 
        
        )
    ai_voice_motion_path = '/icons/ai-voice-motion.gif'
    
    def __init__(self, page, back=None, *args):
        self.page = page
        # self.back = back
        
        
        self.permissionHandler = permissionHandler()
        self.audio_recorder =  ft.AudioRecorder(
            audio_encoder=ft.AudioEncoder.WAV, 
            sample_rate=44100, 
            channels_num=2,
            on_state_changed=ciao
            )
        
        
      
    

        self.Chat_column = ft.Column(
            data = 'null',
            spacing=10, 
            # expand=True,
            # scroll=ft.ScrollMode.HIDDEN, 
            # auto_scroll=True,
            
            controls= [
                ft.Row(expand = True, controls=[ft.Container(expand = True, content = ft.Text(expand = True,spans= [
                        ft.TextSpan(text = '', style=ft.TextStyle(size = 20, color='black54', weight='bold', font_family=font_path+'Exo-Bold.ttf')),
                        ft.TextSpan(text = '', style=ft.TextStyle(size = 14, color='black45', weight='w600')),
                        ft.TextSpan(text = '', style=ft.TextStyle(size = 14, color='#699BE2', weight='w600')),
                        ft.TextSpan(text = '', style=ft.TextStyle(size = 14, color='black45', weight='w600')),
                        
                        ],
                        color='white', size=20, weight='bold', text_align=ft.TextAlign.LEFT))
                        ], 
                       alignment=ft.MainAxisAlignment.CENTER),
                
                ft.Row(controls=[self.mini_bot], alignment=ft.MainAxisAlignment.CENTER)
            ],
            )
       

        self.textinput = ft.TextField(
            border_color=pt['primary'], 
           
            border_radius=12,
            # height=80,
            bgcolor=ft.colors.WHITE,
            max_length=150,
            counter_style=ft.TextStyle(size=10 ,color=ft.colors.GREY_200, weight='w400'),
            # border_width=5,
            # focused_border_color=pt['primary'],
            prefix_icon=ft.icons.CLOUD_CIRCLE_ROUNDED,
             
            hint_text='esprimiti...',
            hint_style=ft.TextStyle(color='black'),
            text_style=ft.TextStyle(color='black'),
            autocorrect=True,
            selection_color=ft.colors.GREEN_100,
            enable_suggestions=True,
            autofocus=True,
            expand=True, 
            on_submit=self.process_text,
            
            on_change=self.switch_text_mode
            
        )

        self.record_button = ft.IconButton(icon=ft.icons.RECORD_VOICE_OVER_ROUNDED, icon_color='black', on_click=self.Registra_audio)
        self.stop_record_button = ft.IconButton(icon=ft.icons.PAUSE_CIRCLE_OUTLINE_OUTLINED, icon_color='black', on_click=self.Registra_audio)
        self.sumbitButton = ft.IconButton(icon=ft.icons.SEND_ROUNDED, icon_color='black', on_click=self.process_text)

        self.buttonContainer =  ft.CircleAvatar(
                            bgcolor='white',
                            
                                    )
        
       
        self.ai_voice_motion = ft.Image(src=self.ai_voice_motion_path, width=300, height=300)
    
        self.dialogTalk= ft.AlertDialog(
            open=True,
            bgcolor=ft.colors.TRANSPARENT, 
            modal=0,
            elevation=0,
            content=ft.Container(
                content=ft.Row(expand=True,alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Image(src='/icons/recording.gif', width=300, height=300)])
                ),
            
            on_dismiss=self.process_text
            )
        
        self.dialogAi_Voice= ft.AlertDialog(
            open=True,
            bgcolor=ft.colors.TRANSPARENT, 
            modal=0,
            elevation=0,
            content=ft.Container(
                content=ft.Row(expand=True,alignment=ft.MainAxisAlignment.CENTER, controls=[self.ai_voice_motion])
                ),
            
            on_dismiss=self.stop_audio
            )
        
        self.page.overlay.append(self.permissionHandler)
        self.page.overlay.append(self.audio_recorder)
        
        # self.set_bars()
        
        super().__init__(
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
            auto_scroll=True,
            controls=[
                
                
            ft.Container(image=ft.DecorationImage(src='/icons/pattern.png', fit=ft.ImageFit.FILL, opacity=0.10),
            padding = 10, 
            expand=True,
            content = self.Chat_column
            
                )
            ]
        )
    
    def set_toolbars(self, *args):
        
        return (
            ft.AppBar(
                    bgcolor='white',
                    center_title=True,
                    elevation_on_scroll=5,
                    leading=ft.Container(
                        border_radius=12,
                        padding=10, 
                        width=80, 
                        height=80, 
                        # border=ft.Border(
                        #     top=ft.BorderSide(3, color=pt['secondary']), 
                        #     bottom=ft.BorderSide(3, color=pt['secondary']), 
                        #     left=ft.BorderSide(3, color=pt['secondary']), 
                        #     right=ft.BorderSide(3, color=pt['secondary'])),
                        
                        content = ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED, icon_color='black87', on_click= lambda _: self.page.go('/'), icon_size=30)),
                    title=ft.Text(value='Psy-AI', size=20, weight='bold', color = ft.colors.BLACK87)
                    ),
            
           
                
           
                ft.BottomAppBar(
                    # expand=True,
                    height=150,
                    bgcolor='white',
                    # surface_tint_color = 'transparent',
                    content=ft.Column(
                        controls = [
                            ft.Container(
                                expand=True,
                                bgcolor='white',
                                border_radius=20,
                                padding = ft.padding.only(left=10, right=10, top=10, bottom=5),
                                # margin=ft.margin.only(bottom=20, left=10, right=10),
                                content = ft.Row(controls=[self.textinput, self.buttonContainer], vertical_alignment=ft.CrossAxisAlignment.CENTER)
                                ),
                            ft.Container()
                        ]
                    )
                ),
                
                ft.FloatingActionButton(
                    content=ft.Icon(name=ft.icons.RECORD_VOICE_OVER_ROUNDED, color=pt['primary'], size=40),
                    bgcolor='white',
                    elevation=10,
                    on_click=self.talk
                ),
        )
            
        
    
    def animate_mini_entro(self, *args):
        import time
        labels = [self.header_text, self.header_text2, self.label, self.label1]
        for i in range(len(labels)):
           if i<len(labels):
               
            for char in labels[i]:
                time.sleep(0.003)
                self.Chat_column.controls[0].controls[-1].content.spans[i].text +=char
                self.Chat_column.controls[0].controls[-1].content.update()
                self.update()
                
   
    
    def talk(self,*args):
        
        # print(self.permissionHandler.check_permission(of=ft.PermissionType.AUDIO))
        if not self.page.web:
            if self.permissionHandler.check_permission(of=ft.PermissionType.AUDIO) == ft.PermissionStatus.GRANTED:
           
                self.page.open(
                    self.dialogTalk
                )
                self.audio_recorder.start_recording(output_path=self._output_path)
            else:
                self.permissionHandler.open_app_settings()
                
        else:
            print('web')
            self.page.open(
                    self.dialogTalk
                )
            self.page.update()
            print(self.audio_recorder.get_input_devices())
            print(self.page.launch_url(self._output_path))
            
    
    def process_text(self, e):
        self.reste_chat_column()
        text =''
        if isinstance(e.control, ft.AlertDialog):
            
            if self.audio_recorder.is_recording():
                print('siiiii')
                self.audio_recorder.stop_recording()
            print('dismiiis')
            text = rc()
            
        else:
            text = self.textinput.value
            
        text_widget = HumanchatWidget(self.page,)
        self.Chat_column.controls.append(text_widget)
        self.Chat_column.update()
        # self.update0
        
        if text is not None:
        
            for char in text:
                text_widget.controls[0].content.value +=char
                if len(text_widget.controls[0].content.value) > 40:
                     text_widget.controls[0].expand = True
                    
                text_widget.controls[0].content.update()
                self.update()
            
            self.reset_fields()
                
        
        
        
        self.Chat_column.controls.append(
            AIchatWidget(page=self.page,text = '....',)
        )
        self.Chat_column.update()
        self.update()
        
        self.passPrompt(text)
        
        
    def passPrompt(self, prompt:str):
        result = ap(user_token=prompt)
        if result is not None:
            threading.Thread(target = self.genera_ai_voice, args =(result,)).start()
            self.Chat_column.controls.pop()
            
            model_response = AIchatWidget(self.page)
            self.Chat_column.controls.append(model_response)
            self.Chat_column.update()
        # self.update()
        
           
            for char in result:
                model_response.controls[-1].content.value +=char
                if len(model_response.controls[-1].content.value) > 40:
                    model_response.controls[-1].expand=True
                model_response.controls[-1].content.update()
                self.update()
             
    def genera_ai_voice(self, text):
        audio_url = tp(text)
        # print()
        self.audio_player = ft.Audio(src=audio_url, autoplay=True, playback_rate=1.30, on_state_changed=self.monitora_stato_audio)
        # self.audio_player.get_duration
        if audio_url is not None:
           
            self.page.open(self.dialogAi_Voice)
            self.page.overlay.append(self.audio_player)
        self.page.update()
                
    def stop_audio(self, *args):
        self.page.overlay.pop()
        self.page.update()
        
    def monitora_stato_audio(self, e):
        if e.data =='completed':
            self.stop_audio()
            self.page.close(self.dialogAi_Voice)
        self.page.update()
            
            
     
        
        
    def switch_text_mode(self, *args):
        
        try:
            
            if self.buttonContainer.content!= self.sumbitButton:
                self.buttonContainer.content = self.sumbitButton
                self.buttonContainer.update()
                self.update()
                
        except Exception as e:
            print(e)
        finally:
            self.buttonContainer.update()
            self.update()
           
    
    
            

    def Registra_audio(self, e):
        if e.control.icon ==ft.icons.RECORD_VOICE_OVER_ROUNDED:
            self.buttonContainer.content = self.stop_record_button
            self.buttonContainer.update()
            self.update()
            # Registra_Audio()
          
     

        elif e.control.icon ==ft.icons.PAUSE_CIRCLE_OUTLINE_OUTLINED:
            self.buttonContainer.content = self.record_button
            self.buttonContainer.update()
            self.update()
            # self.__audio.stop()
          
    # def sumbit(self, *args):
    #     self.Chat_column.controls.append(
    #         chatWidget(page=self.page, position='end', text=self.textinput.value, text_pos='right')
    #     )
    #     self.Chat_column.update()
    #     self.update()

    def reste_chat_column(self,*args):
        if self.Chat_column.data =='null':
            self.Chat_column.controls = []
            self.Chat_column.data = None
            
        self.Chat_column.update()
    
    def reset_fields(self, *args):
        self.textinput.value = ''
        self.buttonContainer.content = None
        self.textinput.update()
        self.buttonContainer.update()
