import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "inter_finalizar_vuelo.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Finaliza_vue(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)# hasta aqui metodos de inicializacion siemore van no los borre
        
        self.b=True
        self.conn=psycopg2.connect(
        host="localhost",
        database ="aeropuertodb",
        user= "postgres",
        password="postgres1" )
        print("Coneccion exitosa")
        self.cursor=self.conn.cursor()

                
        self.agrega()
        self.btn_finalizar.clicked.connect(self.finalizar) #evento de registrar
        self.btn_cancelar.clicked.connect(self.cancelar) #evento de cncelar
          
    def agrega(self):
        self.comboBox_vuelos.clear()
        self.cursor.execute("select * from vuelos where estado ='En Proceso' ;")
        vue = self.cursor.fetchall()
        for ha in vue:
            self.comboBox_vuelos.addItem(str(ha))
      
    # funcion para boton finalizar    
    def finalizar(self):
        #sacamos en variables toda la informacion
        vue=self.comboBox_vuelos.currentText()
        t=""
        for i in vue:
            if i=="(" or i=="'":
                pass
            elif i ==",":
                break 
            else:
                t+=str(i)
       
        msg=QMessageBox()
        # ponemos nombre a la ventana 
        msg.setWindowTitle("Finalizar vuelos")
        # aqui verificamos si el cliente existe 
        if t:
            self.cursor.execute("select hangar from vuelos where id_vuelo ='"+t+"';")
            a=self.cursor.fetchone()
            c=""
            for i in a:
                if i=="(" or i=="'" or i ==")" or i==",":
                    pass
                else:
                    c+=str(i)
            
            self.cursor.execute("update hangares set estado='Libre' where id_hangar='"+c+"';")
            self.conn.commit()
            self.cursor.execute("update vuelos set estado='Finalizado' where id_vuelo ='"+str(t)+"';")
            self.conn.commit()
            msg.setIcon(QMessageBox.Information)
            msg.setText("El vuelo: " +t +" se finalizo satisfactoriamente")
            x=msg.exec_() 
        else:
            msg1=QMessageBox()
            msg1.setWindowTitle("Finalizar vuelos")
            msg1.setIcon(QMessageBox.Information)
            msg1.setText("No hay vuelos en proceso")
            y=msg1.exec_()
        self.comboBox_vuelos.clear()    
        self.agrega()
          
    def cancelar(self):
        self.conn.close()
        self.close()


if __name__ == "__main__":
    
    app =  QtWidgets.QApplication(sys.argv)
    window =Finaliza_vue()
  
    window.show()
    sys.exit(app.exec_())
    
