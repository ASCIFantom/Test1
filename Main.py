from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
import csv
from kivy.uix.button import Button
from kivy.clock import Clock
#from pyjnius import autoclass
from plyer import call




#droid = androidhelper.Android()

#class Droid(self):
	#phone = '0638915414'
	#droid.phoneCallNumber(phone)



Window.size= (480,480)

class MainWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class ThirdWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass



kv = Builder.load_file('Main.kv')


#class Call:
	#tel=+381638915414
	#call.makecall(tel=tel)
	#self._makecall(tel=tel)

	#def _makecall(self,**kwargs):
		#raise NotImplementedError()



class MyGridLayout(Widget):
	started=False
	minutes=0


	def __init__(self,**kwargs):
		super(MyGridLayout,self).__init__(**kwargs)
		Clock.schedule_interval(self.update_time,0)


#Intent = autoclass('android.content.Intent')
#Uri = autoclass('android.net.Uri')
#call = None

	

	def animate_it(self,widget,*args):
		
		animate = Animation(background_color=(1,1,1,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(1,0,0,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(0,0,1,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(1,0,0,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(0,0,1,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(1,0,0,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(0,0,1,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(1,0,0,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(0,0,1,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(1,0,0,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(0,0,1,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(1,0,0,1),opacity= 1, duration=.25,)
		animate += Animation(background_color=(0,0,1,1),opacity= 1, duration=.25,)





		#animate += Animation(background_color=(0,0,0,1),opacity= 1, duration=.5,)

		animate += Animation(blink_size=400)
		animate.bind(on_complite= self.callback)
		#animate += Animation(size_hint=(1,1))
		
		animate.start(widget)

		
	def callback(self,*args):
		animate = Animation(background_color=(1,0,1,1),opacity= 1, duration=.5,)
		


	def press(self,instance):

		#phoneDialNumber  <== androidhelper

		with open('NewInfo.csv','w', newline='') as csv_file:
        		csv_writer = csv.writer(csv_file)
			#csv_writer.writerow(['Latitude:'])
            #csv_writer.writerow(['Longitude:'])
            #csv_writer.writerow(['Broj pretplatnika: ' + '064123456'])
		print('cao')

	def release(self,razgovor):
		pass

		
	#def call_number(self):
		#call = self.Intent()
		#call.setAction(self.Intent.ACTION_CALL)
		#call.setData(self.Uri.parse('tel:%s' % int(0638915414)))
		#self.startActivity(call)

	



class HelpApp(MDApp):
	def build(self):
		return kv


if __name__=='__main__':
	HelpApp().run()