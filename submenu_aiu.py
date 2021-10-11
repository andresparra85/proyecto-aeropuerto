import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from functools import partial
from PyQt5.QtWidgets import*
from inter_registrar_empleado import Registrar_emple
from inter_consultar_empleado import Consulta_empleado
from inter_modificar_empleado import Modifica_empleado

#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "menu_aiu.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Sub_Menu_aiu(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.w1 =Registrar_emple()
        self.w2=Consulta_empleado()
        self.w3=Modifica_empleado()
    
    
        
        self.setupUi(self)
        self.btn_registro_empleado.clicked.connect((partial(self.registra_empleado,self.w1))) #evento de registrar 
        self.btn_consultar_empleado.clicked.connect((partial(self.consulta_empleado,self.w2)))
        self.btn_modificar_empleado.clicked.connect((partial(self.modifica_empleado,self.w3)))

      
    def registra_empleado(self,window):
        window.show()
    
    def modifica_empleado(self,window):
        window.show() 

    def consulta_empleado(self,window):
        window.show()   

      

 
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Sub_Menu_aiu()
    window.show()
    sys.exit(app.exec_())