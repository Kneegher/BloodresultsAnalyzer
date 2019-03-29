import tkinter as tk
import json
import datetime as dt


class App(tk.Tk):

	def __init__(self, *args, **kwargs):

		#App configuration
		tk.Tk.__init__(self, *args, **kwargs)
		self.output_frame = tk.Frame(self)
		self.output_frame.grid(row=0)
		#tk.Grid.rowconfigure(self, 0, weight=1)
		tk.Grid.columnconfigure(self, 600, weight=1)

		with open('save.json', 'r') as file:
			try:
				self.data = json.load(file)
			except:
				self.data = {}
		#Generate output in frame
		self.info_output = tk.Label(self.output_frame, text="READY!")
		self.hb_output_label = tk.Label(self.output_frame, text="Bienvenue!")
		self.sodium_output_label = tk.Label(self.output_frame, text="Écrivez vos résultats")
		self.potassium_output_label = tk.Label(self.output_frame, text="et appuyez sur analyze")
		self.chlore_output_label = tk.Label(self.output_frame, text="pour comprendre vos résultats.")
		self.co2_output_label = tk.Label(self.output_frame, text="Vous pouvez aussi sauvegarder")
		self.calcium_output_label = tk.Label(self.output_frame, text="et charger d'anciens résultats")
		self.phosphore_output_label = tk.Label(self.output_frame, text="en écrivant la date du résultat")
		self.albumine_output_label = tk.Label(self.output_frame, text="et appuyer sur 'load'")
		#Setup label's font
		self.info_output.config(font=("Arial", 25), fg="green")
		self.hb_output_label.config(font=("Arial", 25))
		self.sodium_output_label.config(font=("Arial", 25))
		self.potassium_output_label.config(font=("Arial", 25))
		self.chlore_output_label.config(font=("Arial", 25))
		self.co2_output_label.config(font=("Arial", 25))
		self.calcium_output_label.config(font=("Arial", 25))
		self.phosphore_output_label.config(font=("Arial", 25))
		self.albumine_output_label.config(font=("Arial", 25))
		#Place labels in output_frame
		self.info_output.grid(row=0, column=0)
		self.hb_output_label.grid(row=0, column=1)
		self.sodium_output_label.grid(row=1, column=1)
		self.potassium_output_label.grid(row=2, column=1)
		self.chlore_output_label.grid(row=3, column=1)
		self.co2_output_label.grid(row=4, column=1)
		self.calcium_output_label.grid(row=5, column=1)
		self.phosphore_output_label.grid(row=6, column=1)
		self.albumine_output_label.grid(row=7, column=1)
		input_frame = tk.Frame(self, width=200)
		input_frame.grid(row=0, column=1)

		

		#Generate form
		self.date_label = tk.Label(input_frame, text = "Date: ")
		self.date_entry = tk.Entry(input_frame)
		self.hb_label = tk.Label(input_frame, text = "Hemoglobine: ")
		self.hb_entry = tk.Entry(input_frame)
		self.sodium_label = tk.Label(input_frame, text = "Sodium: ")
		self.sodium_entry = tk.Entry(input_frame)
		self.potassium_label = tk.Label(input_frame, text = "Potassium: ")
		self.potassium_entry = tk.Entry(input_frame)
		self.chlore_label = tk.Label(input_frame, text = "Chlore: ")
		self.chlore_entry = tk.Entry(input_frame)
		self.co2_label = tk.Label(input_frame, text = "CO2: ")
		self.co2_entry = tk.Entry(input_frame)
		self.calcium_label = tk.Label(input_frame, text = "Calcium: ")
		self.calcium_entry = tk.Entry(input_frame)
		self.phosphore_label = tk.Label(input_frame, text = "Phosphore: ")
		self.phosphore_entry = tk.Entry(input_frame)
		self.albumine_label = tk.Label(input_frame, text = "Albumine: ")
		self.albumine_entry = tk.Entry(input_frame)

		#Place form in grid
		self.date_label.grid(row=0, column=0)
		self.date_entry.grid(row=0, column=1)
		self.hb_label.grid(row=1, column=0)
		self.hb_entry.grid(row=1, column=1)
		self.sodium_label.grid(row=2, column=0)
		self.sodium_entry.grid(row=2, column=1)
		self.potassium_label.grid(row=3, column=0)
		self.potassium_entry.grid(row=3, column=1)
		self.chlore_label.grid(row=4, column=0)
		self.chlore_entry.grid(row=4, column=1)
		self.co2_label.grid(row=5, column=0)
		self.co2_entry.grid(row=5, column=1)
		self.calcium_label.grid(row=6, column=0)
		self.calcium_entry.grid(row=6, column=1)
		self.phosphore_label.grid(row=7, column=0)
		self.phosphore_entry.grid(row=7, column=1)
		self.albumine_label.grid(row=8, column=0)
		self.albumine_entry.grid(row=8, column=1)

		#Add today's date to date entry
		today_formated = dt.datetime.today()
		today_formated = today_formated.strftime("%Y-%m-%d")
		self.date_entry.insert(0, today_formated)

		#Generate button
		self.analyze_button = tk.Button(input_frame, text="Analyze", command=self.analyze_sequence, width=20, height=3)
		self.analyze_button.grid(row=10, sticky="W")
		self.close_button = tk.Button(input_frame, text="Close", command=self.destroy, width=20, height=3)
		self.close_button.grid(row=10, column=1, sticky="W")
		self.save_button = tk.Button(input_frame, text="Save", command=self.save_sequence, width=20, height=3)
		self.save_button.grid(row=11, sticky="W")
		self.load_button = tk.Button(input_frame, text="Load", command=self.load_sequence, width=20, height=3)
		self.load_button.grid(row=11, column=1, sticky="W")

	def analyze_sequence(self):
		"""Launch and drive the analyze sequence"""
		self.info_output['text'] = 'Analyzing...'
		self.info_output['fg'] = 'yellow'
		user_input = self.get_input()
		user_input = user_input[next(iter(user_input))]
		print(user_input)
		result_dict = self.check_difference(user_input)
		output = self.create_output(result_dict)
		self.send_output(output)
		self.info_output['text'] = 'Analyzed!'
		self.info_output['fg'] = 'green'

	def save_sequence(self):
		"""Formats the data and adds it to the save"""
		input_json = self.get_input()
		date = self.date_entry.get()

		try:
			self.data[date]
		except KeyError:
			if "ERROR" in input_json[date].values() or "EMPTY" in input_json[date].values():
				self.info_output['text'] = 'ERROR!\nAnalyze to see'
				self.info_output['fg'] = 'red'
			else:
				self.data[date] = input_json[date]
				with open('save.json', 'w') as file:
					json.dump(self.data, file)
				self.info_output['text'] = 'Saved!'
				self.info_output['fg'] = 'green'
		else:
			self.info_output['text'] = 'ERROR!\nDate Already Exist'
			self.info_output['fg'] = 'red'

	def load_sequence(self):
		"""Loads the data from the date in the entry"""
		date = str(self.date_entry.get())
		try:
			self.change_entry_values(self.data[date])
			self.info_output['text'] = 'Loaded!'
			self.info_output['fg'] = 'green'
			self.analyze_sequence()
		except KeyError:
			self.info_output['text'] = 'ERROR!\nDate Doesn\'t Exist'
			self.info_output['fg'] = 'red'
			
	def change_entry_values(self, values):
		"""Fast way to change the values of the entry with a dict"""
		self.hb_entry.delete(0, 'end')
		self.hb_entry.insert(0, values['hemoglobine'])
		self.sodium_entry.delete(0, 'end')
		self.sodium_entry.insert(0, values['sodium'])
		self.potassium_entry.delete(0, 'end')
		self.potassium_entry.insert(0, values['potassium'])
		self.chlore_entry.delete(0, 'end')
		self.chlore_entry.insert(0, values['chlore'])
		self.co2_entry.delete(0, 'end')
		self.co2_entry.insert(0, values['co2'])
		self.calcium_entry.delete(0, 'end')
		self.calcium_entry.insert(0, values['calcium'])
		self.phosphore_entry.delete(0, 'end')
		self.phosphore_entry.insert(0, values['phosphore'])
		self.albumine_entry.delete(0, 'end')
		self.albumine_entry.insert(0, values['albumine'])

	def get_input(self):
		"""Retireve the input from the GUI and verifies it"""
		input_list = []
		date = str(self.date_entry.get())
		input_list.append(self.hb_entry.get())
		input_list.append(self.sodium_entry.get())
		input_list.append(self.potassium_entry.get())
		input_list.append(self.chlore_entry.get())
		input_list.append(self.co2_entry.get())
		input_list.append(self.calcium_entry.get())
		input_list.append(self.phosphore_entry.get())
		input_list.append(self.albumine_entry.get())

		counter = 0
		for item in input_list:
			if item == "" or item == "EMPTY":
				input_list[counter] = "EMPTY"
				counter += 1
			elif "." in item:
				input_list[counter] = float(item)
				counter += 1
			elif item.isdigit() == False or item == "ERROR":
				input_list[counter] = "ERROR"
				counter += 1
			else:
				input_list[counter] = float(item)
				counter += 1

		input_dict ={
		date: {
			"hemoglobine": input_list[0],
			"sodium": input_list[1],
			"potassium": input_list[2],
			"chlore": input_list[3],
			"co2": input_list[4],
			"calcium": input_list[5],
			"phosphore": input_list[6],
			"albumine": input_list[7]
			}}

		return input_dict

	def check_difference(self, input_dict):
		"""Check difference between input values and reference values"""
		reference = {
			"hemoglobine": (100, 115),
			"sodium": (130, 145),
			"potassium": (3.5, 5.5),
			"chlore": (98, 110),
			"co2": (21, 31),
			"calcium": (2.01, 2.55),
			"phosphore": (1.01, 1.70),
			"albumine": (35, 50)
		}

		result_dict = {
			"hemoglobine": "",
			"sodium": "",
			"potassium": "",
			"chlore": "",
			"co2": "",
			"calcium": "",
			"phosphore": "",
			"albumine": ""	
		}

		for key, value in input_dict.items():
			lower_value = reference[key][0]
			higher_value = reference[key][1]

			if value == "EMPTY":
				result_dict[key] = "EMPTY"
			elif value == "ERROR":
				result_dict[key] = "ERROR"
			else:
				if value >= lower_value and value <= higher_value:
					result_dict[key] = "NORMAL"
				elif value < lower_value and value > lower_value - (0.07*lower_value):
					result_dict[key] = "LOW"
				elif value > higher_value and value < higher_value + (0.07*higher_value):
					result_dict[key] = "HIGH"
				elif value <= lower_value - (0.07*lower_value):
					result_dict[key] = "LOWER"
				elif value >= higher_value + (0.07*higher_value):
					result_dict[key] = "HIGHER"
				else:
					result_dict[key] = "ERROR"

		return result_dict

	def create_output(self, some_dict):
		"""Create the text for the output"""
		output_list = []
		for key, value in some_dict.items():
			if value == "HIGHER":
				self.change_output_color(key, "RED")
				output_list.append("^^Votre " + key + " est en haut de la limite suggéré.")
			elif value == "HIGH":
				self.change_output_color(key, "orange")
				output_list.append("^Votre " + key + " est légèrement en haut de la limite suggéré.")
			elif value == "NORMAL":
				self.change_output_color(key, "green")
				output_list.append("-Votre " + key + " est dans les normes!")
			elif value == "LOW":
				self.change_output_color(key, "orange")
				output_list.append("_Votre " + key + " est légèrement en bas de la limite suggéré.")
			elif value == "LOWER":
				self.change_output_color(key, "red")
				output_list.append("__Votre " + key + " est en bas de la limite suggéré.")
			elif value == "EMPTY":
				self.change_output_color(key, "grey")
				output_list.append("Votre " + key + " est vide.")
			elif value == "ERROR":
				self.change_output_color(key, "grey")
				output_list.append("*Il y a une erreur avec votre " + key)
		return output_list

	def change_output_color(self, key, color):
		"""Changes the color of the label"""
		if key == "hemoglobine":
			self.hb_output_label.config(fg=color)
		elif key == "sodium":
			self.sodium_output_label.config(fg=color)
		elif key == "potassium":
			self.potassium_output_label.config(fg=color)
		elif key == "chlore":
			self.chlore_output_label.config(fg=color)
		elif key == "co2":
			self.co2_output_label.config(fg=color)
		elif key == "calcium":
			self.calcium_output_label.config(fg=color)
		elif key == "phosphore":
			self.phosphore_output_label.config(fg=color)
		elif key == "albumine":
			self.albumine_output_label.config(fg=color)

	def send_output(self, output_list):
		"""Sends the output to the GUI"""
		self.hb_output_label["text"] = output_list[0]
		self.sodium_output_label["text"] = output_list[1]
		self.potassium_output_label["text"] = output_list[2]
		self.chlore_output_label["text"] = output_list[3]
		self.co2_output_label["text"] = output_list[4]
		self.calcium_output_label["text"] = output_list[5]
		self.phosphore_output_label["text"] = output_list[6]
		self.albumine_output_label["text"] = output_list[7]

my_app = App()
my_app.title("Blood result analyzer")
my_app.geometry("1320x400")
my_app.mainloop()






