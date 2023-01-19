from tkinter import *
from tkinter.messagebox import *
from insertar import insertar_persona
base = Tk()
base.resizable(False,False)
#base.geometry('400x600')
# variables
dni = StringVar()
name = StringVar()
last_name = StringVar()
edad = StringVar()
mail = StringVar()
estatura = StringVar()
# etiquetas 
label_dni = Label(base, text='cedula: ').grid(column =0, row=1, padx =10, pady=10)
label_name = Label(base, text='Nombre: ').grid(column =0, row=2, padx =10, pady=10)
label_apellido = Label(base, text='Apellido: ').grid(column =0, row=3, padx =10, pady=10)
label_edad = Label(base, text='Edad: ').grid(column =0, row=4, padx =10, pady=10)
label_mail = Label(base, text='Email: ').grid(column =0, row=5, padx =10, pady=10)
label_estatura = Label(base, text='Estatura: ').grid(column =0, row=6, padx =10, pady=10)
# entry
entry_dni = Entry(base, textvariable=dni).grid(column = 2, row=1,padx =10, pady=10)
entry_name = Entry(base, textvariable=name).grid(column = 2, row=2,padx =10, pady=10)
entry_apellido = Entry(base, textvariable=last_name).grid(column = 2, row=3,padx =10, pady=10)
entry_edad = Entry(base, textvariable= edad).grid(column = 2, row=4,padx =10, pady=10)
entry_mail = Entry(base, textvariable=mail).grid(column = 2, row=5,padx =10, pady=10)
entry_estatura = Entry(base, textvariable=estatura).grid(column = 2, row=6,padx =10, pady=10)

# btn de guardar y cancelar
def guardar():
    showinfo('Guardar', f"{dni.get()}, {name.get()}, {last_name.get()}, {edad.get()}, {mail.get()}, {estatura.get()}")
    insertar_persona(dni.get(), name.get(), last_name.get(), edad.get(),mail.get(), estatura.get())
    limpiar_campos()

btn_guardad = Button(text='Guardar', width=10, command=guardar).grid(column=0,row=7, padx=10, pady=10)

def limpiar_campos():
    dni.set("")
    name.set("")
    last_name.set("")
    edad.set("")
    mail.set("")
    estatura.set("")
  
btn_cancelar = Button(text='Cancelar', width=10, command=limpiar_campos).grid(column=2,row=7, padx=10, pady=10)
base.mainloop()