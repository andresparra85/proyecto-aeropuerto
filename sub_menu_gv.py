import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from functools import partial
from PyQt5.QtWidgets import*
from inter_facturar_vuelo import Factura_vuelo
from inter_consultar_vuelo_emple_mos import Consulta_vuelo_e_m


#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "menu_gv.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Sub_Menu_gv(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.w1 =Factura_vuelo()
        self.w2=Consulta_vuelo_e_m()
   
    
    
        
        self.setupUi(self)
        self.btn_factura_vuelo.clicked.connect((partial(self.factura,self.w1))) #evento de registrar 
        self.btn_consulta_vuelo.clicked.connect((partial(self.consulta,self.w2)))
        

      
    def factura(self,window):
        window.show()
    

    def consulta(self,window):
        window.show()   

      

 
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Sub_Menu_gv()
    window.show()
    sys.exit(app.exec_())