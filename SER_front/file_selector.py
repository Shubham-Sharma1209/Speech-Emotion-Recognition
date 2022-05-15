from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class Filechooser(FloatLayout):
	def select(self, *args):
		try: 
			self.label.text = args[1][0]
		except: pass
        
        
class FileApp(App):
	def build(self):
		return Filechooser()

Builder.load_file('file_sel.kv')
if __name__ == '__main__':
	FileApp().run()
