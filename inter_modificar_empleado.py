import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
from functools import partial
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner
qtCreatorFile = "inter_modificar_empleado.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.
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
        self.lineEdit_cedula.returnPressed.connect(self.genera_datos)
        self.btn_modificar.clicked.connect(self.modifica_datos) 
        self.btn_cancelar.clicked.connect(self.cancelar)         

    def modifica_datos(self):
        ced=self.lineEdit_cedula.text()
        b=True
        if self.lineEdit_nombre.text()=="":
            b=False
        if self.lineEdit_cedula.text()=="":
            b=False    
        nom=self.lineEdit_nombre.text()
        tel=self.lineEdit_telefono.text()
        correo=self.lineEdit_correo.text()
        direc=self.lineEdit_direccion.text()
        sueldo=self.lineEdit_sueldo.text()
        fecha=self.lineEdit_fecha.text()
        est=self.comboBox_estado.currentText()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar empleado")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_cedula(ced):
            if b:
                self.genera_datos()
                self.cursor.execute("update empleados set nombre ='"+nom+"',telefono='"+tel+"',correo='"+correo+"',direccion='"+direc+"',sueldo='"+sueldo+"',fecha_ingreso='"+fecha+"',estado='"+est+"'  where cedula='"+ced+"';")
                self.conn.commit()
                msg.setText("El empleado con cedula : "+ced+" se modifico correctamente")
            else:
                msg.setText("Campos vacios")
        else :
            msg.setText("El empleado con cedula : "+ced+" no se encuentra registrado")
        x=msg.exec_()   
        self.limpiar() 

    def limpiar(self):
        self.lineEdit_cedula.clear()
        self.lineEdit_nombre.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_correo.clear()
        self.lineEdit_direccion.clear()
        self.lineEdit_fecha.clear()    
        self.lineEdit_sueldo.clear()  
        
        
          

    def verifica_cedula(self,ced):
        sql="select * from empleados where cedula ='"+ced+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False
                       
    def genera_datos(self):
        ced =self.lineEdit_cedula.text()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar empleado")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_cedula(ced):


            self.cursor.execute("select nombre,telefono,correo,direccion,sueldo,fecha_ingreso,estado from empleados where cedula='"+ced+"';")  
            a=self.cursor.fetchone()
            nombre,telefono,correo,direccion,sueldo,fecha_ingreso,estado=" "," "," "," "," "," "," "
            c=[nombre,telefono,correo,direccion,sueldo,fecha_ingreso,estado]
            for i in range(len(a)):
                c[i]=a[i]  

            self.lineEdit_nombre.setText(str(c[0]))
            self.lineEdit_telefono.setText(str(c[1]))
            self.lineEdit_correo.setText(str(c[2]))
            self.lineEdit_direccion.setText(str(c[3]))   
            self.lineEdit_sueldo.setText(str(c[4]))
            self.lineEdit_fecha.setText(str(c[5]))
            if str(c[6])=='Activo':
                self.comboBox_estado.setCurrentIndex(0)  
            else:
                self.comboBox_estado.setCurrentIndex(1)
            self.lineEdit_sueldo.setValidator(QtGui.QDoubleValidator())
            self.lineEdit_telefono.setValidator(QtGui.QDoubleValidator())    
        else:
            msg.setText("El empleado con cedula : "+ced+" no se encuentra registrado")
            x=msg.exec_() 

        
    def cancelar(self):
        self.close()    




if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Modifica_empleado()
    window.show()
    sys.exit(app.exec_())        