import tkinter as tk

# La clase Tk() representa la ventana principal ( Objeto )

ventana = tk.Tk() # Instanciamos el objeto 
ventana.title('Mi primer ventana en python !!') # Titulo de la ventana
ventana.geometry('900x600') # Tamaño de la ventana en px
ventana.configure(bg='#0ce42c') #Color del fondo de la ventana 

def click():
    print('Boton presionado')

boton = tk.Button(ventana , text='Clic aqui', command=click)
boton.configure(bg="#e4370c",padx=10 , pady=10)



boton.pack()


ventana.mainloop()

