import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from functools import partial
from PyQt5.QtWidgets import*
from inter_registrar_cliente import Registre_clien
from inter_consultar_cliente import Consultar_cliente
from inter_visualizar_clientes import visualiza_clientes
from inter_modificar_cliente import Modifica_cliente


#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "menu_ic.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Sub_Menu_ic(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.w1 =Registre_clien()
        self.w2=Consultar_cliente() 
        self.w3 =Modifica_cliente()
        self.w4=visualiza_clientes()     
        self.setupUi(self)
        self.btn_cliente.clicked.connect((partial(self.registra,self.w1))) #evento de registrar 
        self.btn_consulta.clicked.connect((partial(self.consulta,self.w2)))
        self.btn_modifica.clicked.connect((partial(self.modi,self.w3))) #evento de registrar 
        self.btn_visualizar.clicked.connect((partial(self.visuali,self.w4)))
                
      
    def registra(self,window):
        window.show()
    
    def consulta(self,window):
        window.show()   

    def visuali(self,window) :
        window.visualizar()
        window.show() 

    def modi(self,window) :
        window.show()       
         
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Sub_Menu_ic()
    window.show()
    sys.exit(app.exec_())