import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2

qtCreatorFile = "inter_registrar_empleado.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Registrar_emple(QtWidgets.QMainWindow, Ui_MainWindow):
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
        self.texto()
        self.agrega_anios()
        self.btn_registrar.clicked.connect(self.registrar) 
        self.btn_cancelar.clicked.connect(self.cancelar) 
        self.lineEdit_sueldo.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_edad.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_telefono.setValidator(QtGui.QDoubleValidator())

    def verifica_cedula(self,ced):
        sql="select * from empleados where cedula ='"+ced+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False     

    def registrar(self):
        b=True
        ced=self.lineEdit_cedula.text()
        if self.lineEdit_cedula.text()==" ":
            b=False
        nom=self.lineEdit_nombre.text()
        tel=self.lineEdit_telefono.text()
        correo=self.lineEdit_correo.text()
        direc=self.lineEdit_direccion.text()
        edad=self.lineEdit_edad.text()
        sueldo=self.lineEdit_sueldo.text()
        fecha=self.comboBox_dia.currentText()+"/"+self.comboBox_mes.currentText()+"/"+self.comboBox_anio.currentText()
        est="Activo"
        
        msg=QMessageBox()
        msg.setWindowTitle("Registro de Empleados")
        if self.verifica_cedula(ced) is False:
            msg.setIcon(QMessageBox.Information)
            msg.setText("El empleado: " +nom +" con Cedula : " + ced+ 
                " se registro satisfactoriamente")
            self.cursor.execute("INSERT INTO empleados VALUES " \
            "('"+ced+"','"+nom+"','"+tel+"','"+correo+"','"+direc+"','"+edad+"','"+sueldo+"','"+fecha+"','"+est+"')")       
            self.conn.commit()    
        elif b:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Campos vacios ")
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setText("La cedula:  " + ced+ 
                " ya se encuentra registrada con otro empleado")    

        x=msg.exec_()    
        self.limpiar()

    def texto(self):
        self.lineEdit_cedula.setPlaceholderText("Digite la cédula")
        self.lineEdit_nombre.setPlaceholderText("Digite el nombre")
        self.lineEdit_telefono.setPlaceholderText("Digite el teléfono")
        self.lineEdit_correo.setPlaceholderText("Digite el correo")
        self.lineEdit_direccion.setPlaceholderText("Digite la dirección")
        self.lineEdit_edad.setPlaceholderText("Digite la edad")
        self.lineEdit_sueldo.setPlaceholderText("Digite el sueldo")

    def limpiar(self):
        self.lineEdit_cedula.clear()
        self.lineEdit_nombre.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_correo.clear()
        self.lineEdit_direccion.clear()
        self.lineEdit_edad.clear()    
        self.lineEdit_sueldo.clear()  
    
    def agrega_anios(self):
        i=2021
        while i>1900:
            self.comboBox_anio.addItem(str(i))
            i=i-1

    def cancelar(self):
        self.conn.close()
        self.close()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Registrar_emple()
    window.show()
    sys.exit(app.exec_())



