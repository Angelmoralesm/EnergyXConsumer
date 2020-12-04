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
#entry = tk.Entry(win)
#entry.grid(row=10,column=1,padx=5,pady=10,ipady=3)
#entry.pack(pady=170) 
#entry.insert(0,"Username")
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
def Search():
	finded=True
	#busqueda dentro de base de datos
	data_base = open("data.txt", "r")
	for line in data_base.readlines():#lee linea por linea
		list_aux = line.split()
		if "EMPY" in line:
			finded = False
			
	data_base.close()
	
	if finded == False:
		register()
	else:
		operation(list_aux)

def register():
	#Funcion refresh cambia variables en menu desplegable
	def refresh(num):
		# Reset var and delete all old options
		marca_opt2['menu'].delete(0, 'end')
		# Insert list of new options (tk._setit hooks them up to var)
		if num == 1:
			new_choices = ('Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9')
			varMod.set('Ryzen 3')
		elif num == 2:
			new_choices = ('core i3', 'core i5', 'core i7', 'core i9')
			varMod.set('core i3')
			
		for choice in new_choices:
			marca_opt2['menu'].add_command(label=choice, command=tk._setit(varMod, choice))

#Las funciones denominadas fun_opt(n) son encargadas de actualizar los valores de las listas deslizables
	def fun_opt2(event):
		if varMod.get() == 'core i3':
			print("okA")
		elif varMod.get() == 'Ryzen 3':
			print ("rizen oka")	
	def fun_opt1(event):
		if marca.get() == 'AMD':
			print(list_mod)
			refresh(1)
		elif marca.get()=='Intel':
			print(list_mod)
			refresh(2)

	def presentation():
		label_hello= Label(win, text="Hello welocome to Energy Consumer",width = 20)
		label_hello.pack()
	presentation()
	entry_hours = tk.Entry(win,width=3)
	#entry_hours.grid(row=1,column=1,padx=3,pady=1,ipady=3)
	entry_hours.pack(pady=10)
	entry_hours.insert(0,"")
	entry_hours.place(x=150,y=10)
	label_ask = Label(win, text = "Regular Hours of use:") 
	label_ask.place(x=1,y=10)
	global marca
	opciones_marca = ['Intel','AMD']
	marca=tk.StringVar()
	global varMod
	list_mod = ['core i3','core i5','core i7','core i9']
	varMod=tk.StringVar()
	marca.set(opciones_marca[0])
	varMod.set(list_mod[0])
	marca_opt = tk.OptionMenu(win,marca,*opciones_marca,command = fun_opt1)
	marca_opt2 = tk.OptionMenu(win,varMod,*list_mod , command = fun_opt2)
	marca_opt.config(width=6)
	marca_opt2.config(width=6)
	marca_opt.place(x=100,y=40)
	marca_opt2.place(x=60,y=80)
	label_model = Label(win, text = "Model")
	label_m = Label(win, text = "manufacturer")
	label_m.place(x=1,y=45)
	label_model.place(x=1,y=85)
#Search funciona como funcion principal, la cual dirige el flujo de la aplicacion	
#Monitor 40w a 60w
Search()
global button 
global button_login
win.mainloop() 
