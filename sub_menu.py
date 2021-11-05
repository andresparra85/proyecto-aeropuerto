import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from functools import partial
from PyQt5.QtWidgets import*
from inter_registrar_hangar import Registrar_hangar
from inter_registrar_vuelo import Registre_vuelo
from inter_finalizar_vuelo import Finaliza_vue
from inter_modificar_vuelo import Modifica_vuelo
from inter_consultar_vuelo import Consulta_vuelo
from inter_modificar_hangar import Modifica_hangar
from inter_visualizar_vuelos import visualiza_vuelos

#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "sub_menu.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Sub_Menu_av(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.w1 =Registrar_hangar()
        self.w2=Registre_vuelo()
        self.w3=Finaliza_vue()
        self.w4=Modifica_vuelo()
        self.w5=Consulta_vuelo()
        self.w6=Modifica_hangar()
        self.w7=visualiza_vuelos()
        
        self.setupUi(self)
        self.btn_registro_hangar.clicked.connect((partial(self.registra_hangar,self.w1))) #evento de registrar
        self.btn_registro_vuelo.clicked.connect((partial(self.registra_vues,self.w2)))   
        self.btn_finalizo_vuelos.clicked.connect((partial(self.finaliza_vues,self.w3)))   
        self.btn_modifica_vuelos.clicked.connect((partial(self.modifica_vuelo,self.w4))) 
        self.btn_consulta_vuelos.clicked.connect((partial(self.consulta_vuelo,self.w5)))
        self.btn_modifica_hangar.clicked.connect((partial(self.modifica_hangar,self.w6)))
        self.btn_visualizar.clicked.connect((partial(self.visu,self.w7)))

      
    def registra_hangar(self,window):
        window.show()
    def registra_vues(self,window):
        window.todos()
        window.show()    
    def finaliza_vues(self,window):
        window.agrega()
        window.show()   
    
    def modifica_vuelo(self,window):
        window.show() 

    def consulta_vuelo(self,window):
        window.show()   

    def modifica_hangar(self,window):
        window.show()  

    def visu(self,window):
        window.visualizar()
        window.show()  

 
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Sub_Menu_av()
    window.show()
    sys.exit(app.exec_())