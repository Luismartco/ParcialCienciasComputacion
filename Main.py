import subprocess 
import tkinter as tk

def abrir_ventana1():
    subprocess.Popen(['python', 'Simple.py'])

def abrir_ventana2():
    subprocess.Popen(['python', 'Multiple.py'])

ventana = tk.Tk()
ventana.title("Ventana principal") 
ventana.minsize(400, 300)
ventana.maxsize(400, 300)

etiqueta = tk.Label(ventana,text="Tarea Parcial Primer Corte")
etiqueta.grid(row=1,column=1,padx=5,pady=5)
etiquetaa = tk.Label(ventana,text="Ciencias de la computación")
etiquetaa.grid(row=2,column=1,padx=5,pady=5)

etiqueta1 = tk.Label(ventana,text="Abrir requerimiento 1:")
etiqueta1.grid(row=3,column=1,padx=5,pady=5)
boton1 = tk.Button(ventana, text="RL Simple", command=abrir_ventana1)
boton1.grid(row=4, column=1, padx=5, pady=5) 


etiqueta2 = tk.Label(ventana,text="Abrir requerimiento 2:")
etiqueta2.grid(row=3,column=2,padx=5,pady=5)
boton2 = tk.Button(ventana, text="RL Multiple", command=abrir_ventana2)
boton2.grid(row=4, column=2, padx=5, pady=5) 

ventana.mainloop()
