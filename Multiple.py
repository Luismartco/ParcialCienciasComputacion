import tkinter as tk
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

# Creación del set de datos
data = {
    'Tiempo': [15, 20, 12, 25, 18],
    'Duracion': [30, 25, 20, 35, 28],
    'Personal': [3, 2, 4, 2, 3],
    'Satisfaccion': [8, 7, 9, 6, 7]
}

df = pd.DataFrame(data)

X = df[['Tiempo', 'Duracion', 'Personal']]
Y = df[['Satisfaccion']]

# División de los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=40)

# Modelo de regresión lineal
model = LinearRegression()

# Entrenamiento
model.fit(x_train, y_train)

# Función para calcular la predicción y mostrar el resultado
def predecir_satisfaccion():
    try:
        tiempo = float(caja_tiempo.get())
        duracion = float(caja_duracion.get())
        personal = float(caja_personal.get())
        
        # Crear los nuevos valores para la predicción
        valores_nuevos = np.array([[tiempo, duracion, personal]])
        satisfaccion_predicha = model.predict(valores_nuevos)
        
        resultado.config(text=f'Satisfacción predicha: {satisfaccion_predicha[0][0]:.2f}')
    
    except ValueError:
        resultado.config(text="Por favor, ingrese valores válidos.")

# Creación de la ventana
ventana = tk.Tk()
ventana.title("Regresión Lineal Múltiple")
ventana.minsize(400, 300)
ventana.maxsize(400, 300)

# Etiquetas y cajas de entrada
etiqueta_tiempo = tk.Label(ventana, text="Digite el Tiempo:")
etiqueta_tiempo.grid(row=1, column=1, padx=5, pady=5)
caja_tiempo = tk.Entry(ventana)
caja_tiempo.grid(row=1, column=2, padx=5, pady=5)

etiqueta_duracion = tk.Label(ventana, text="Digite la Duración:")
etiqueta_duracion.grid(row=2, column=1, padx=5, pady=5)
caja_duracion = tk.Entry(ventana)
caja_duracion.grid(row=2, column=2, padx=5, pady=5)

etiqueta_personal = tk.Label(ventana, text="Digite el Personal:")
etiqueta_personal.grid(row=3, column=1, padx=5, pady=5)
caja_personal = tk.Entry(ventana)
caja_personal.grid(row=3, column=2, padx=5, pady=5)

# Botón para calcular la predicción
boton_predecir = tk.Button(ventana, text="Predecir satisfacción", command=predecir_satisfaccion)
boton_predecir.grid(row=4, column=2, padx=5, pady=5)

# Label para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado")
resultado.grid(row=5, column=1, padx=5, pady=5)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
