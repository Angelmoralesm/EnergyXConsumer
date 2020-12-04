# /usr/bin/env python
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import threading
import platform
from tkinter.ttk import *
import time
import os
import psutil
porcent_aux = psutil.cpu_percent()
time.sleep(1)
battery=psutil.sensors_battery()
porcent = psutil.cpu_percent()
cpu_number=psutil.cpu_count(logical=True)
print(battery)
#oss=platform.system()
win = tk.Tk()
win.title("Energy consumer")
win.iconphoto(False, tk.PhotoImage(file='icon.png'))
win.geometry("400x450")
win.resizable(False,False)
global entry
entry = tk.Entry(win)
entry.grid(row=10,column=1,padx=5,pady=10,ipady=3)
entry.pack(pady=170) 
entry.insert(0,"Username")
global label_message

def operation(list_aux):
	print(list_aux)
	watts= list_aux[1]
	watts2 = int(watts)
	kw= float(watts2/1000)
	horas_de_uso=list_aux[2]
	horas =  int(horas_de_uso)
	dias = 20
	kwh = kw * horas * dias
	print(kwh)
	gasto_mensual = 105*kwh
	print(gasto_mensual)
	#xd = os.system('')
	#print(xd)
def message():
	username = entry.get();
	entry.delete(0, 'end')
	finded=False
	#busqueda dentro de base de datos
	data_base = open("data.txt", "r") 
	username_aux = username.replace(" ", "")#Elimina espacios al usuario para indexar base de datos
	for line in data_base.readlines():#lee linea por linea
		list_aux = line.split()#transforma la linea
		if list_aux.count(username_aux) != 0:
			finded = True
			button.destroy()
			button_login.destroy()
			entry.destroy()
			operation(list_aux)
			#print("encontrado")
	
	data_base.close()
	
	if finded == False:
		not_found = "not found " + username
		label_message = Label(win, text = not_found)	
		label_message.pack(pady=10)
		print("n")
		#ingreso manual de datos

def register():

	def fun_opt1(event):
		if marca.get() == 'AMD':
			print("works")
			varMod=['Ryzen 3','Ryzen 5','Ryzen 7','Ryzen 9' ]
			print(varMod)
		elif marca.get()=='Intel':
			varMod=['core i3','core i5','core i7','core i9' ]
			print("works intel")
			print(varMod)
	button.destroy()
	button_login.destroy()
	entry.destroy()
	entry_hours = tk.Entry(win,width=3)
	entry_hours.grid(row=1,column=1,padx=3,pady=1,ipady=3)
	entry_hours.pack(pady=10)
	entry_hours.insert(0,"")
	entry_hours.place(x=150,y=10)
	label_ask = Label(win, text = "Regular Hours of use:") 
	label_ask.place(x=1,y=10)
	global marca
	opciones_marca = ['Intel','AMD']
	marca=tk.StringVar()
	global varMod
	marca.set(opciones_marca[0])
	marca_opt = tk.OptionMenu(win,marca,*opciones_marca,command = fun_opt1 )
	marca_opt.config(width=3)
	marca_opt.place(x=100,y=40)
	label_m = Label(win, text = "manufacturer")
	label_m.place(x=1,y=40)
        
global button		 
global button_login
button = tk.Button(win, text = " Sign in", height = 1, command = register,background = "#4ef5af")
button_login = tk.Button(win, text = "Login", height = 1, command = message,background = "#4ef5af")
button.place(x=200, y=200)
button_login.place(x=125,y=200)
win.mainloop() 
