import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.graphics import Rectangle,Color
from kivy.lang import Builder
from kivy.core.text import LabelBase
from file_selector import FileApp
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics','resizable',True)
        
    
class MainWidget(Widget):
    f_path=StringProperty()
    addr=StringProperty()
    Show_Emo=StringProperty()
    Show_Emo="NO EMOTION"
    addr=""+"NO FILE SELECTED"
    def display_add(self):
        try:      
            # f_path=fs.path
            # print(f_path) 
            self.addr=show_popup()
            if self.addr=='':
                self.addr='Cannot Load Files'
        except:
            self.addr="Cannot locate files"
        x=TextInput(text=self.addr,size_hint=(0.5,0.5),size=(dp(220),dp(40)),disabled=True,pos=(dp(420),dp(460)))
        self.add_widget(x)
    def emo(self):
        self.Show_Emo="Cant detect emotion: No files"
        return self.Show_Emo


def show_popup():
    show = Filechooser()
    popupWindow = Popup(title ="Select a file",content =show,size =(400, 400),pos=(0,0))
    
    popupWindow.open()
    print(show.f_path)
    return show.f_path

class Filechooser(FloatLayout): 
	def select(self, *args):
		try: 
			self.label.text = args[1][0]
		except: pass

class front_pageApp(App):
    pass

LabelBase.register(name='Georgia',fn_regular='Georgia Regular font.ttf')
Builder.load_file('front_page.kv')

front_pageApp().run()   