from turtle import Screen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.graphics import Rectangle,Color
from kivy.lang import Builder
from kivy.core.text import LabelBase


Config.set('graphics','resizable',True)

class BoxLayoutExample(BoxLayout):
    pass
        
    
class MainWidget(Widget):
    addr=StringProperty()
    Show_Emo=StringProperty()
    Show_Emo="NO EMOTION"
    addr=""+"NO FILE SELECTED"
    def display_add(self):
        self.addr="Cannot locate files"
        x=TextInput(text=self.addr,size_hint=(0.5,0.5),size=(dp(220),dp(40)),disabled=True,pos=(dp(420),dp(460)))
        self.add_widget(x)
        
    def emo(self):
        self.Show_Emo="Cant detect emotion: No files"
        # return self.Show_Emo


class front_pageApp(App):
    pass

LabelBase.register(name='Georgia',fn_regular='Georgia Regular font.ttf')
Builder.load_file('front_page.kv')
front_pageApp().run()