import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from hangar import Hangar
from PyQt5.QtWidgets import*
import psycopg2
qtCreatorFile = "inter_registrar_hangar.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Registrar_hangar(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.b=True
        self.conn=psycopg2.connect(
        host="localhost",
        database ="aeropuertodb",
        user= "postgres",
        password="postgres1" )
        print("Coneccion exitosa")

        self.cursor=self.conn.cursor()

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #self.lineEdit_id_hangar.setValidator(QtGui.QDoubleValidator())# metodo para restringir solo numeros
        self.lineEdit_area_hangar.setValidator(QtGui.QDoubleValidator())
        self.texto()
        self.btn_registrar.clicked.connect(self.registrar) 
        self.btn_cancelar.clicked.connect(self.cancelar) 
     

    def registrar(self):
        b1=True
        if self.lineEdit_id_hangar.text()==" ":
            b1=False

        if self.lineEdit_area_hangar.text()==" ":
            b1=False    

        id=self.lineEdit_id_hangar.text()
        area=self.lineEdit_area_hangar.text()
        est="Libre"
        hangar=Hangar(id,area)
        msg=QMessageBox()
        msg.setWindowTitle("Registro de Hangares")
        if self.verifica_hangar(id):
            msg.setIcon(QMessageBox.Information)
            msg.setText("El hangar con id: " +id+" de área : " +area+ 
                " se registro satisfactoriamente")
            self.cursor.execute("INSERT INTO hangares VALUES " \
            "('"+id+"','"+area+"','"+est+"')")       
            self.conn.commit()    
        elif b1:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Campos vacios")
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setText("El hangar con id:  " +id+ 
                " ya se encuentra registrado")    

        x=msg.exec_()    
        self.limpiar()
        
        
    def verifica_hangar(self,id):

        sql="select * from hangares where id_hangar='"+id+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        if len(a)>0:
            return False
        else:
            return True  
    def texto(self):
        self.lineEdit_id_hangar.setPlaceholderText("Digite el id del hangar")
        self.lineEdit_area_hangar.setPlaceholderText("Digite el área del hangar")

    def limpiar(self):
        self.lineEdit_id_hangar.clear()
        self.lineEdit_area_hangar.clear() 

    def cancelar(self):
        if self.b:
            self.conn.close()
        self.close()


if __name__ == "__main__":

    app =  QtWidgets.QApplication(sys.argv)
    window =Registrar_hangar()
    window.show()
    sys.exit(app.exec_())

