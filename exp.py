# /usr/bin/env python
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import threading
import platform
import subprocess
from tkinter.ttk import *

os=platform.system()
win = tk.Tk()
win.title("Energy consumer")
win.iconphoto(False, tk.PhotoImage(file='icon.png'))
win.geometry("400x450")
win.resizable(False,False)
global entry
entry = tk.Entry(win)
entry.grid(row=10,column=1,padx=5,pady=10,ipady=3)
entry.pack(pady=170) 
entry.insert(0,"Your PC model name")


def operation(list_aux):
	print(list_aux)
	print("yeahhh boyy")
	
	watts= list_aux[1]
	print(watts)
	
	
def message():
	model = entry.get();
	entry.delete(0, 'end')
	finded=False
	#busqueda dentro de base de datos
	data_base = open("data.txt", "r") 
	model_aux = model.replace(" ", "")#Elimina espacios al modelo para indexar base de datos
	for line in data_base.readlines():#lee linea por linea
		list_aux = line.split()#transforma la linea
		if list_aux.count(model_aux) != 0:
			finded = True
			button.destroy()
			entry.destroy()
			operation(list_aux)
			#print("encontrado")
	
	data_base.close()
	
	if finded == False:
		not_found = "not found " + model
		label_message = Label(win, text = not_found)
		
		label_message.pack(pady=10)
		label_message.config(bg="red")
		print("no encontrado")		
		#ingreso manual de datos
		

global button		 
button = tk.Button(win, text = "Start", height = 1, command = message,background = "#4ef5af")
button.place(relx=0.5, rely=0.5, anchor=CENTER)


win.mainloop()

