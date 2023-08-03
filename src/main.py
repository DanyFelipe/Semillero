import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from personajeUI import Ui_pjCreator  # Importa la clase generada desde ui_mi_ventana.py

from Mago import Mago

class MiVentana(QMainWindow, Ui_pjCreator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":

    mago = Mago("Taelwin", 300, "Masculino", "Elfo")
    habilidades_mago = mago.habilidades()

    # Imprimir cada habilidad en una línea
    for habilidad in habilidades_mago:
        print(habilidad)

    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())