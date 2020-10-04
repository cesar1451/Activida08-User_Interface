from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot #Identificar cuando se ejecute el evento del boton
from ui_mainwindow import Ui_MainWindow #Importar libreria de la interfaz del designer en .py

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow() #crear un objeto de una vista del designer
        ui.setupUi(self) #Las configuraciones que se hacen se incrustan en el objeto
        ui.pushButton.clicked.connect(self.click_agregar) #Decirle que cuando le de click se conecte a la función
    
    @Slot() #Decirle que la siguiente función detectara eventos click
    def click_agregar(self):
        print('click')