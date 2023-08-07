import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from ComprasDiscosUI import Ui_Form
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Connection import conectar, insertar_compra, print_resultados, obtener_albumes  # Importa la clase generada desde ui_mi_ventana.py

class MiVentana(QMainWindow, Ui_Form):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableView = self.findChild(QTableView, 'tableView')
        self.pushButtonComprar.clicked.connect(self.realizar_y_mostrar)
        
    def mostrar_en_tabla(self, resultados):
        model = QStandardItemModel(len(resultados), 6)
        model.setHorizontalHeaderLabels(["Nombre del Cliente", "Teléfono", "Álbum Comprado", 
                                         "Grupo del Álbum", "Cantidad de Albums", "Total Precio"])

        for row, data in enumerate(resultados):
            for col, value in enumerate(data):
                item = QStandardItem(str(value))
                model.setItem(row, col, item)

        self.tableView.setModel(model)    
        
    def mostrar_tabla(self):
        conn = conectar()
        if conn:
            telefono_cliente = self.lineEdit_tel.text()
            resultados = print_resultados(conn, telefono_cliente)
            conn.close()

            if resultados:
                self.mostrar_en_tabla(resultados)  
                
    def realizar_y_mostrar(self):
        conn = conectar()
        if conn:
            insertar_compra(conn,ventana)
            self.mostrar_tabla()             
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()

    # -------------------------- COMBOBOX CONSULTA
    conn = conectar()
    if conn:
        albumes = obtener_albumes(conn)
        if albumes:
            for album_id, album_nombre in albumes:
                ventana.comboBoxDiscos.addItem(album_nombre, album_id)
        else:
            print("No se pudieron obtener los álbumes")
    else:
        print("No se pudo conectar") 

    ventana.show()
    sys.exit(app.exec_())