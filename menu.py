import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from functools import partial
from PyQt5.QtWidgets import*
from sub_menu import Sub_Menu_av
from submenu_aiu import Sub_Menu_aiu
from sub_menu_gv import Sub_Menu_gv
from sub_menu_ic import Sub_Menu_ic
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "menu.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Menu(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.w1 =Sub_Menu_ic()
        self.w2 =Sub_Menu_aiu()
        self.w3_1 =Sub_Menu_av()
        self.w4=Sub_Menu_gv()
        
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
        window.w1.todos()
        window.show()      
        
            
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    
    window =Menu()
    window.show()
    sys.exit(app.exec_())