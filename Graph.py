import tkinter as tk
import datetime as dt
import matplotlib.pyplot as plt
import json

class app(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.frame = tk.Frame(self, width=50, height=10)
		self.frame.pack()

		self.data = self.load_data()

		self.hb_button = tk.Button(self.frame, text="Hemoglobine", command= lambda: self.launch_graph('hemoglobine'))
		self.sodium_button = tk.Button(self.frame, text="Sodium", command= lambda: self.launch_graph('sodium'))
		self.potassium_button = tk.Button(self.frame, text="Potassium", command= lambda: self.launch_graph('potassium'))
		self.chlore_button = tk.Button(self.frame, text="Chlore", command= lambda: self.launch_graph('chlore'))
		self.co2_button = tk.Button(self.frame, text="CO2", command= lambda: self.launch_graph('co2'))
		self.calcium_button = tk.Button(self.frame, text="Calcium", command= lambda: self.launch_graph('calcium'))
		self.phosphore_button = tk.Button(self.frame, text="Phosphore", command= lambda: self.launch_graph('phosphore'))
		self.albumine_button = tk.Button(self.frame, text="Albumine", command= lambda: self.launch_graph('albumine'))
		self.hb_button.grid(row=0)
		self.sodium_button.grid(row=1)
		self.potassium_button.grid(row=2)
		self.chlore_button.grid(row=3)
		self.co2_button.grid(row=4)
		self.calcium_button.grid(row=5)
		self.phosphore_button.grid(row=6)
		self.albumine_button.grid(row=7)

	def load_data(self):
		with open('save.json', 'r') as file:
			data = json.load(file)
		return data

	def launch_graph(self, substance):
		X = self.organize_x()
		Y = self.organize_y(substance)
		plt.scatter(X, Y)
		plt.xlim(X[0]-dt.timedelta(days=3), X[len(X)-1]+dt.timedelta(days=3))
		plt.ylim(Y[0]-(Y[0]*0.10), Y[len(Y)-1]+(Y[len(Y)-1]*0.10))
		plt.show()

	def organize_x(self):
		X = []
		for key in self.data.keys():
			X.append(dt.datetime.strptime(key, '%Y-%m-%d'))
		return X

	def organize_y(self, substance):
		Y = []
		for key, value in self.data.items():
			Y.append(self.data[key][substance])
		return Y
		


my_app = app()
my_app.mainloop()