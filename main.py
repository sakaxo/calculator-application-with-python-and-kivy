from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
#from kivy.config import Config


Window.size = (300,500)
#Config.set('kivy','window_icon','img/equals.png')

class CalculatorScreen(Widget):
	def clear(self):
		""" clearn all characters in TextInput """
		self.ids.input_data.text = ''

	def clearn_last_character(self):
		""" clearn the last character in TextInput """
		last_char_removed = self.ids.input_data.text[ : -1]
		self.ids.input_data.text = last_char_removed

	def pressed_button(self, pressed):
		pressed = str(pressed)
		value_before = self.ids.input_data.text

		# check input text for 0 and take the right action
		if value_before is not '0':
			self.ids.input_data.text = f"{value_before}{pressed}"			

		else:
			self.ids.input_data.text = pressed

	

	def dot_button_pressed(self):
		value_before = self.ids.input_data.text
		sign_list = ['+', '-','*',u'\xf7']

		def dot_handler(sign):
			
			num_list = value_before.split(sign)

			if sign in value_before and "." not in num_list[-1]:

				self.ids.input_data.text = f"{value_before}."

			elif '.' in value_before:
				pass
			else:
				self.ids.input_data.text = f"{value_before}."

		for sign in sign_list:
			dot_handler(sign)


	def equals(self):
		# get expression from TextInput and evaluate
		expression = self.ids.input_data.text
		try:
			
			if "%" in expression:
				expression = expression.replace('%', '/100')

			if u'\xf7' in expression:
				expression = expression.replace(u'\xf7', '/')

			result = eval(expression)

			# update value in TextInput
			self.ids.input_data.text = str(result)
		except ZeroDivisionError:
			# can't devide by 0
			self.ids.input_data.text = "Can\'t devide by 0"
		except:
			self.ids.input_data.text = "Error!"
		
		
		




class Calculator(App):
	"""Main Calculator app"""
	def build(self):
		self.title = "Calculator app"
		self.icon = "equals.png"
		return CalculatorScreen()



if __name__ == '__main__':
	Calculator().run()