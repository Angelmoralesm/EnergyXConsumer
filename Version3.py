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
from os import remove

#porcent_aux = psutil.cpu_percent()
time.sleep(1)
#battery=psutil.sensors_battery()
#porcent = psutil.cpu_percent()
#cpu_number=psutil.cpu_count(logical=True)
#print(battery)
#oss=platform.system()
win = tk.Tk()
win.title("Energy consumer")
win.iconphoto(False, tk.PhotoImage(file='icon.png'))
win.geometry("400x450")
win.resizable(False,False)
#background_image=tk.PhotoImage(file='icon.png')
#background_label = tk.Label(win, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
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
	var_watt = tk.StringVar(win)
	var_watt.set(watts2)
	print(var_watt.get())
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
		if "EMPTY" in line:
			finded = False
			
	data_base.close()
	
	if finded == False:
		presentation()
	else:
		operation(list_aux)

def register():
	#Funcion refresh cambia variables en menu desplegable
	def refresh_2(serie):
		marca_opt3['menu'].delete(0, 'end')
		
		if serie == 'Ryzen 3':
			new_choices = ('4300U','3250U','3250C','3300URadeonVega6','3200URadeonVega3','2300URadeonVega6','2200URadeonVega3')
			varSerie.set('4300U')
		if serie == 'Ryzen 5':
			new_choices = ('4600U','4500U','3450U','3550HRadeonVega8','3500URadeonVega8','3500C','600H','2500URadeonVega8')
			varSerie.set('4600U') 
		if serie == 'Ryzen 7':
			new_choices = ('4800H','4800U','4700U','3700C','3750HRadeonRXVega10','3700URadeonRXVega10','2800H','27300URadeonVega10')
			varSerie.set('4800H')
		if serie == 'Ryzen 9':
			new_choices = ('4900HS')
			varSerie.set('4900HS')
		
		if serie == 'core i3':
			new_choices = ('1115G4','9300','8300','6100U')
			varSerie.set('1115G4')
		if serie == 'core i5':
			new_choices = ('1135G7','10400','9600T','8265U')
			varSerie.set('1115G7') 
		if serie == 'core i9':
			new_choices = ('10900','8950HK','9980HK','10900XX','9920XX','9940XX')
			varSerie.set('10900')
		if serie == 'core i7':
			new_choices = ('10875H','6560U')
			varSerie.set('10875H')
		if serie == 'Celeron':
			new_choices = ('G5900','J4025','N3450')
			varSerie.set('G5900')
		if serie == 'Pentium':
			new_choices = ('GoldG6500','GoldG5500','D1508','J3710')
			varSerie.set('GoldG6500')
			
		for choice in new_choices:
			marca_opt3['menu'].add_command(label=choice, command=tk._setit(varSerie, choice))
	
	def refresh(num):
		# Reset var and delete all old options
		marca_opt2['menu'].delete(0, 'end')
		# Insert list of new options (tk._setit hooks them up to var)
		if num == 1:
			new_choices = ('Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9')
			varMod.set('Ryzen 3')
			refresh_2(varMod.get())
		elif num == 2:
			new_choices = ('Core i3', 'Core i5', 'Core i7', 'Core i9','Pentium','Celeron')
			varMod.set('Core i3')
			refresh_2(varMod.get())
			
		for choice in new_choices:
			marca_opt2['menu'].add_command(label=choice, command=tk._setit(varMod, choice))

#Las funciones denominadas fun_opt(n) son encargadas de actualizar los valores de las listas deslizables
	
	def fun_opt3(event):
		print("nothing")

	def fun_opt2(event):
		if varMod.get() == 'Core i3':
			print(varMod.get())
			refresh_2(varMod.get())
		if varMod.get() == 'Core i5':
			print(varMod.get())
			refresh_2(varMod.get())
		if varMod.get() == 'Core i7':
			print(varMod.get())
			refresh_2(varMod.get())
		if varMod.get() == 'Core i9':
			print(varMod.get())
			refresh_2(varMod.get())
		if varMod.get() == 'Pentium':
			print(varMod.get())
			refresh_2(varMod.get())
		if varMod.get() == 'Celeron':
			print(varMod.get())
			refresh_2(varMod.get())
		
		if varMod.get() == 'Ryzen 3':
			print(varMod.get())	
			refresh_2(varMod.get())
		if varMod.get() == 'Ryzen 5':
			print(varMod.get())	
			refresh_2(varMod.get())
		if varMod.get() == 'Ryzen 7':
			print(varMod.get())	
			refresh_2(varMod.get())
		if varMod.get() == 'Ryzen 9':
			print(varMod.get())	
			refresh_2(varMod.get())
			
	def fun_opt1(event):
		if marca.get() == 'AMD':
			print(varMod.get())
			refresh(1)
		elif marca.get()=='Intel':
			print(varMod.get())
			refresh(2)
	   #### Send Button #### 

	def sig_in():
		remove('data.txt')
		file = open("data.txt", "w+") 
		#for i in range(10):
		name=name_entry.get()
		name_aux = name.replace(" ", "")
		file.write(name_aux)
		file.write(" 200 ")
		file.write(str(hours.get()))
		file.write(" ")
		#varMod.replace(" ","")
		m=marca.get()
		v=varMod.get()
		v_aux=	v.replace(" ","")
		s=varSerie.get()
		file.write(m)
		file.write(v_aux)
		file.write(s)
		file.write(" ")
		file.write(use.get())
		file.close()

		Send_button.destroy()
		label_usr.destroy()
		label_ask.destroy()
		hours_opt.destroy()
		label_type_use.destroy()
		use_opt.destroy()
		label_name.destroy()
		name_entry.place_forget()
		label_processor.place_forget()
		marca_opt.destroy()
		marca_opt2.destroy()
		marca_opt3.destroy()
		label_model.place_forget()
		label_m.place_forget()
		label_serie.place_forget()

		Search()
	
	Send_button = tk.Button(win, text = "Sign in",command = sig_in, height = 1,background = "#4ef5af")
	Send_button.place(x=155,y=350)

	#### Use information #####
	
	label_usr = Label(win,text="User information")
	label_usr.place(x=140,y=150)
	label_usr.config(font=("Helvetica",10,'bold'))

	label_ask = Label(win, text = "Regular Hours of use in a day:") 
	label_ask.place(x=5,y=175)
	hours_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
	hours= tk.IntVar()
	hours.set(hours_list[0])
	hours_opt = tk.OptionMenu(win,hours,*hours_list)
	hours_opt.place(x=210,y=170)

	label_type_use = Label(win, text = "Type of use:") 
	label_type_use.place(x=5,y=215)
	use_list = ['Oficce','Design','Gamer','Multimedia']
	use= tk.StringVar()
	use.set(use_list[0])
	use_opt = tk.OptionMenu(win,use,*use_list)
	use_opt.place(x=100,y=210)

	label_name = Label(win, text = "Username:")
	label_name.place(x=5,y=250)
	name_entry = tk.Entry(win)
	name_entry.place(x=100,y=250)

	###### Procesador information #####
	
	global marca
	global varMod
	global serie

	label_processor = Label(win,text="Processor information")
	label_processor.place(x=125,y=5)
	label_processor.config(font=("Helvetica",10,'bold'))
	
	opciones_marca = ['Intel','AMD']
	list_mod = ['core i3','core i5','core i7','core i9','Pentium','Celeron']
	opciones_serie =['1115G4','9300','8300','6100U']
	
	marca=tk.StringVar()
	varMod=tk.StringVar()
	varSerie=tk.StringVar()
	
	marca.set(opciones_marca[0])
	varMod.set(list_mod[0])
	varSerie.set(opciones_serie[0])
	
	marca_opt = tk.OptionMenu(win,marca,*opciones_marca,command = fun_opt1)
	marca_opt2 = tk.OptionMenu(win,varMod,*list_mod , command = fun_opt2)
	marca_opt3 = tk.OptionMenu(win,varSerie,*opciones_serie,command = fun_opt3)
	
	marca_opt.config(width=6)
	marca_opt2.config(width=6)
	marca_opt3.config(width=6)
	
	marca_opt.place(x=100,y=30)
	marca_opt2.place(x=60,y=70)
	marca_opt3.place(x=60,y=110)
	
	label_model = Label(win, text = "Model: ")
	label_m = Label(win, text = "manufacturer: ")
	label_serie = Label(win, text="Serie: ")
	
	label_m.place(x=5,y=35)
	label_model.place(x=5,y=75)
	label_serie.place(x=5,y=115)

#Search funciona como funcion principal, la cual dirige el flujo de la aplicacion	
#Monitor 40w a 60w

def presentation():

	def change_text1():
		
		def change_text2():
			
			def change_text3():

				def change_text4():

					def change_text5():
						def change_text7():
							strings.set(' ')
							button7.destroy()
							register()

						def change_text6():
							strings.set('are you ready?')
							button6.destroy()
							global button7
							button7 = tk.Button(win, text = "lets do it", height = 1, command = change_text7,background = "#4ef5af")
							button7.place(x=155,y=200)
						
						strings.set('So, we want to help you\n to monitor and raise awareness\n about your pc energy consump')
						button5.destroy()
						button6 = tk.Button(win, text = "Ok", height = 1, command = change_text6,background = "#4ef5af")
						button6.place(x=175,y=200)
					
					strings.set('And you pay for energy, right?')
					button4.destroy()
					button5 = tk.Button(win, text = "Right", height = 1, command = change_text5,background = "#4ef5af")
					button5.place(x=175,y=200)
				
				strings.set('THAT IS A LOT OF ENERGY!!')
				button3.destroy()
				button4 = tk.Button(win, text = "Yes", height = 1, command = change_text4,background = "#4ef5af")
				button4.place(x=175,y=200)	
			
			strings.set('The american population\n averaged nearly 12,000 kilowatt-hours (kWh)\n of electricity consumption\n per person in 2017')
			button2.destroy()
			button3 = tk.Button(win, text = "Next", height = 1, command = change_text3,background = "#4ef5af")
			button3.place(x=175,y=200)
		
		strings.set('According to international energy statistics\n from the US Energy Information Administration (EIA),\n global electricity consumption\n continues to increase\n faster than the world population')
		button1.destroy()
		button2 = tk.Button(win, text = "Next", height = 1, command = change_text2,background = "#4ef5af")
		button2.place(x=175,y=200)

	print("something")
	strings=tk.StringVar(win)
	strings.set('Welcome to \nEnergy consumer beta version')
	label_Hello = tk.Label(win, textvariable=strings)
	label_Hello.place(x=200,y=100,anchor=CENTER)
	label_Hello.config(font=("Courier",10))
	button1 = tk.Button(win, text = "Next", height = 1, command = change_text1,background = "#4ef5af")
	button1.place(x=175, y=200)
Search()
win.mainloop() 
