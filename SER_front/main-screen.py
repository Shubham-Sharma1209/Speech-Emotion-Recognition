from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder 
from kivy.config import Config
from kivy.properties import StringProperty,ObjectProperty
from kivy.core.text import LabelBase    
from kivy.uix.popup import Popup
<<<<<<< HEAD
from kivy.core.window import Window
=======
>>>>>>> 0e433b9d7cb71c1f2c75439130b2ea43b36f5c8d

Window.size=(600,600)
Config.set('graphics','resizable',True)
<<<<<<< HEAD


=======
>>>>>>> 0e433b9d7cb71c1f2c75439130b2ea43b36f5c8d
class Main_screen(FloatLayout):
    file_path=StringProperty('Currently No files')

    def call_adrr(self):
        try:
            self.the_popup = FileChoosePopup(load=self.load)
            self.the_popup.open()
        except:
            self.file_path='Cannot Select files'
<<<<<<< HEAD
        
=======
>>>>>>> 0e433b9d7cb71c1f2c75439130b2ea43b36f5c8d

    def load(self, selection):
        self.file_path = str(selection[0])
        self.the_popup.dismiss()
<<<<<<< HEAD
=======
        # print(self.file_path)

        # if self.file_path:
        #     self.ids.get_file.text = self.file_path
>>>>>>> 0e433b9d7cb71c1f2c75439130b2ea43b36f5c8d

    def emo(self):
        self.Show_Emo="Cant detect emotion: No files"
        return self.Show_Emo
<<<<<<< HEAD


class FileChoosePopup(Popup):
    load = ObjectProperty()
=======
>>>>>>> 0e433b9d7cb71c1f2c75439130b2ea43b36f5c8d

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

<<<<<<< HEAD
class SER(App):
    def build(self):
        return Main_screen()
    
LabelBase.register(name='Georgia',fn_regular='Georgia Regular font.ttf')
LabelBase.register(name='Georgia Bold',fn_regular='georgia bold.ttf')    
Builder.load_file('front_page.kv')
if __name__=='__main__':
    SER().run()

=======
>>>>>>> 0e433b9d7cb71c1f2c75439130b2ea43b36f5c8d
