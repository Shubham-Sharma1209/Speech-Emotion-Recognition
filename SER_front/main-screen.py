from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder 
from kivy.config import Config
from kivy.properties import StringProperty,ObjectProperty
from kivy.core.text import LabelBase    
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.size=(600,600)
Config.set('graphics','resizable',True)


class Main_screen(FloatLayout):
    file_path=StringProperty('Currently No files')

    def call_adrr(self):
        try:
            self.the_popup = FileChoosePopup(load=self.load)
            self.the_popup.open()
        except:
            self.file_path='Cannot Select files'
        

    def load(self, selection):
        self.file_path = str(selection[0])
        self.the_popup.dismiss()

    def emo(self):
        self.Show_Emo="Cant detect emotion: No files"
        return self.Show_Emo


class FileChoosePopup(Popup):
    load = ObjectProperty()


class SER(App):
    def build(self):
        return Main_screen()
    
LabelBase.register(name='Georgia',fn_regular='Georgia Regular font.ttf')
LabelBase.register(name='Georgia Bold',fn_regular='georgia bold.ttf')    
Builder.load_file('front_page.kv')
if __name__=='__main__':
    SER().run()

