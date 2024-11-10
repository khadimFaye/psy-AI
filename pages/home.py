
import flet as ft

font_path = '/fonts/Exo/static/assets/fonts/Exo/static/'


class Home(ft.Column):
    descrizione = 'Psy-AI è il tuo assistente psicologico virtuale, sempre pronto a darti supporto emotivo con empatia e discrezione. Qui puoi esprimerti liberamente, trovare consigli positivi e ritrovare un po\'di serenità, senza mai sentirti giudicato.'
    def __init__(self, page, *args):
        self.page = page
        self.mini_bot = ft.Image(
            src = '/icons/mini-bot.gif',
            filter_quality=ft.FilterQuality.HIGH,
            height=100,
        animate_opacity=ft.Animation(duration=20, curve=ft.AnimationCurve.EASE_IN,), 
            animate_scale=ft.Animation(duration=100, curve=ft.AnimationCurve.BOUNCE_IN_OUT,), 
            
            )
        super().__init__(
            scroll=ft.ScrollMode.HIDDEN,
            expand=True,
            auto_scroll=True,
           
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
            controls=[
                

                ft.Row(controls=[ft.Container(content= ft.Image(src='/icons/bigbot.png', fit=ft.ImageFit.FILL, width=300, height=300))], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Container(height = 180),
                ft.Column( spacing =0,alignment=ft.MainAxisAlignment.CENTER, controls=[
                   
                    # ft.Row(controls=[ft.Image(src='/icons/psyai.png', fit = ft.ImageFit.CONTAIN, width=200, height=200)], alignment=ft.MainAxisAlignment.START),
                    ft.Row(controls=[self.mini_bot], alignment=ft.MainAxisAlignment.START),
                    # ft.Row(controls=[ft.Text(value ='Psy-AI', color='white', size=30, weight='bold')], alignment=ft.MainAxisAlignment.START),
                    ft.Row(expand = True, controls=[ft.Text(value = self.descrizione, expand = True, color='black45', size=16 if self.page.platform.value !='windows' or not self.page.web else 20, weight='w600', text_align=ft.TextAlign.LEFT)], alignment=ft.MainAxisAlignment.CENTER),
                ]),
            ft.Container(height = 10),
            ft.Row(controls=[
                ft.Container(
                    padding = 5, 
                    content = ft.ElevatedButton(
                        height=50, 
                        expand = True, 
                        on_click = lambda _ : self.page.go('chat'),
                        content =ft.Text(font_family=font_path+'Exo-Bold.ttf',value = 'avvia seduta!', color='black87',size=18, weight='bold'), bgcolor=ft.colors.WHITE,))], alignment=ft.MainAxisAlignment.CENTER,)
            ],


            
        )