from pages.chat import Chat
from pages.home import Home
import flet as ft
import threading



views = {
    
    'chat' : Chat,
    '/' : Home,
    
}

def change_route(page:ft.Page ,route:str = None):
    route = route or page.route
    page.views.clear()
    update_page(page, route)
    
def update_page(page:ft.Page, route):
    dtn =  views[route](page)
    view = None
    if route =='chat':
        view = ft.View(controls=[ft.SafeArea(content =ft.Container(content=dtn, padding=10, expand=True), expand=True),], padding=0,  bgcolor='#F6F7F8')
        page.views.append(view)
        page.update()
        view.appbar, view.bottom_appbar, view.floating_action_button = dtn.set_toolbars()
        threading.Thread(target=dtn.animate_mini_entro).start()
        view.update()
        return 1
    
    view = ft.View(controls=[ft.Container(content = ft.SafeArea(content =dtn, expand=True), expand=True, padding=10,)], padding=0, auto_scroll=True, bgcolor='white')
   
    page.views.append(view)
    page.update()
    
    
   
        
       
    
    
    
    
       
       