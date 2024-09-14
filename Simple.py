import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Creación del set de datos
data = {
    'pacientes': [20, 25, 18, 30, 22],
    'tiempo': [15, 20, 12, 25, 18]
}

df = pd.DataFrame(data)
x = df[['pacientes']]
y = df[['tiempo']]

# Entrenamiento del modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

# Función para calcular y mostrar el resultado
def simple():
    try:
        n1 = float(caja1.get())
        pas_nuevo = np.array([[n1]])
        time_predecido = model.predict(pas_nuevo)
        
        resultado.config(text=f'El tiempo predicho para {n1} pacientes: {time_predecido[0][0]:.2f}')
        
        # Gráfica los datos y la línea de regresión
        plt.scatter(x, y)
        plt.title('Pacientes VS Tiempo')
        plt.xlabel('Pacientes')
        plt.ylabel('Tiempo')
        plt.plot(x, model.predict(x), color='yellow')
        plt.scatter(pas_nuevo, time_predecido, color='red')
        plt.show()
    
    except ValueError:
        resultado.config(text="Por favor, ingrese un número válido.")

# Creación de la ventana
ventana = tk.Tk()
ventana.title("Regresión Lineal Simple")
ventana.minsize(400, 300)
ventana.maxsize(400, 300)

# Etiquetas y cajas de entrada
etiqueta1 = tk.Label(ventana, text="Digite la cantidad de pacientes:")
etiqueta1.grid(row=2, column=1, padx=5, pady=5)
caja1 = tk.Entry(ventana)
caja1.grid(row=2, column=2, padx=5, pady=5)

# Botón para calcular
boton1 = tk.Button(ventana, text="Calcular tiempo", command=simple)
boton1.grid(row=3, column=2, padx=5, pady=5)

# Label para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado")
resultado.grid(row=4, column=1, padx=5, pady=5)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()