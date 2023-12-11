import sys
from PyQt5.QtWidgets import QApplication
from classes.usuario import Usuario
from sql.sql_functions import *
from graphic_interface.ventana_login import LoginApp
import tkinter as tk

def main():
    app = QApplication(sys.argv)

    conexion = connect_db()
    
    # Try catch
    cursor = get_cursor(conexion)

    root = tk.Tk()
    app = LoginApp(root, cursor)
    root.mainloop()

if __name__ == '__main__':
    main()