import tkinter as tk
from tkinter import messagebox

class AppSaludo:
    # Ejemplo de GUI con multiples componentes
    def __init__(self, root):
        self.root = root
        self.root.title('App Saludo - POO con GUI')
        self.root.geometry('500x350')
        self.root.configure(bg='#09cbdc')
        self._crear_widgets()

    def _crear_widgets(self):
        # Se crea etiqueta Label 
        self.lbl_nombre = tk.Label(
            self.root, text='Ingresa tu nombre: ', bg='#EAF4FB', font=('Arial',12)
        )
        self.lbl_nombre.grid(row=0, column=0, padx=20, pady=20, sticky='w' )

        # Campo de entrada 
        self.entry_nombre = tk.Entry(
            self.root, width=25, relief=tk.SOLID, bd=1, font=('Arial',12)
        )
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=20)

        # Bóton
        self.btn_Saludar= tk.Button(
            self.root, text='Saludar', command=self.saludar,
            bg='#2E74B5', fg='white', font=('Arial', 12, 'bold'),
            relief=tk.FLAT, padx=15, pady=5, cursor='hand2'
        )
        self.btn_Saludar.grid(row=1, column=0, columnspan=2, pady=10)

        # Area de texto 
        self.txt_resultado = tk.Text(
            self.root, height=5, width=40, font=('Arial', 11), 
            relief=tk.SOLID,
            bd=1, state=tk.DISABLED
        )
        self.txt_resultado.grid(row=2, column=0,
                                columnspan=2, padx=20, pady=10)


    def saludar(self):
        nombre = self.entry_nombre.get().strip()
        if nombre:
            mensaje = f'¡Hola {nombre}! Binvenido/a'
            self.txt_resultado.config(state=tk.NORMAL)
            self.txt_resultado.insert(tk.END, mensaje)
            self.txt_resultado.config(state=tk.DISABLED
    )
        else:
            messagebox.showwarning('Advertencia', 'Por favor ingresa tu nombre')

# Punto de entrada principal

if __name__ == '__main__':
    ventana= tk.Tk()
    app = AppSaludo(ventana)
    ventana.mainloop()