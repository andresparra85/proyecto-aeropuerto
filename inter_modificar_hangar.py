import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
from functools import partial
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner
qtCreatorFile = "inter_modificar_hangar.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja
class Modifica_empleado(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)# hasta aqui metodos de inicializacion siemore van no los borre

        self.conn=psycopg2.connect(
        host="localhost",
        database ="aeropuertodb",
        user= "postgres",
        password="postgres1" )
        print("Coneccion exitosa")
        self.cursor=self.conn.cursor()
        self.line=QLineEdit()
        self.lineEdit_id_hangar.returnPressed.connect(self.genera_datos)
        self.btn_modificar.clicked.connect(self.modifica_datos) 
        self.btn_cancelar.clicked.connect(self.cancelar)         

    def modifica_datos(self):
        id_hangar=self.lineEdit_id_hangar.text()
        b=True
        if self.lineEdit_area.text()=="":
            b=False
        if self.lineEdit_id_hangar.text()=="":
            b=False    
        area=self.lineEdit_area.text()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar hangar")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_id_hangar(id_hangar):
            if b:
                self.genera_datos()
                self.cursor.execute("update hangares set area ='"+area+"' where id_hangar='"+id_hangar+"';")
                self.conn.commit()
                msg.setText("El hangar con ID : "+id_hangar+" se modifico correctamente")
            else:
                msg.setText("Campos vacios")
        else :
            msg.setText("El hangar con ID : "+id_hangar+" no se encuentra registrado")
        x=msg.exec_()   
        self.limpiar() 

    def limpiar(self):
        self.lineEdit_id_hangar.clear()
        self.lineEdit_area.clear()
          

    def verifica_id_hangar(self,id_hangar):
        sql="select * from hangares where id_hangar ='"+id_hangar+"';"
        self.cursor.execute(sql)
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False
                       
    def genera_datos(self):
        id_hangar =self.lineEdit_id_hangar.text()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar hangar")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_id_hangar(id_hangar):

            self.cursor.execute("select area from hangares where id_hangar='"+id_hangar+"';")  
            a=self.cursor.fetchone()
            area=" "
            c=[area]
            for i in range(len(a)):
                c[i]=a[i]  

            self.lineEdit_area.setText(str(c[0]))
            self.lineEdit_area.setValidator(QtGui.QDoubleValidator()) 
        else:
            msg.setText("El hangar con ID : "+id_hangar+" no se encuentra registrado")
            x=msg.exec_() 

        
    def cancelar(self):
        self.close()    




if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Modifica_empleado()
    window.show()
    sys.exit(app.exec_())        