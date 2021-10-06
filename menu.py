import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from functools import partial
from PyQt5.QtWidgets import*
from inter_registrar_cliente import Registre_clien
from inter_registrar_empleado import Registrar_emple
from inter_registrar_vuelo import Registre_vuelo
from inter_finalizar_vuelo import Finaliza_vue
from inter_facturar_vuelo import Factura_vuelo
from sub_menu import Sub_Menu
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "menu.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Menu(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.w1 =Registre_clien()
        self.w2 =Registrar_emple()
        self.w3_1 =Sub_Menu()
        self.w4=Factura_vuelo()
        
        self.setupUi(self)
        self.btn_admi_clies.clicked.connect((partial(self.adminitra_cliets,self.w1))) #evento de registrar
        self.btn_admi_empleados.clicked.connect((partial(self.adminitra_emples,self.w2)))   
        self.btn_gestioneTa.clicked.connect((partial(self.adminitra_vuelo,self.w3_1)))     
        self.btn_gestione.clicked.connect((partial(self.factura_vuelo,self.w4)))  

    def adminitra_cliets(self,window):
        window.show()
    def adminitra_emples(self,window):
        window.show()    
    def adminitra_vuelo(self,window):
        window.show()      
    def factura_vuelo(self,window):
        window.todos()
        window.show()      
        
            
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    
    window =Menu()
    window.show()
    sys.exit(app.exec_())