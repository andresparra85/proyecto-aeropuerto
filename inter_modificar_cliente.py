import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
from functools import partial
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner
qtCreatorFile = "inter_modificar_cliente.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja
class Modifica_cliente(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
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
        fecha=self.lineEdit_fecha.text()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar cliente")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_cedula(ced):
            if b:
                self.genera_datos()
                self.cursor.execute("update clientes set nombre ='"+nom+"',telefono='"+tel+"',correo='"+correo+"',direccion='"+direc+"',fecha_nacimiento='"+fecha+"';")
                self.conn.commit()
                msg.setText("El cliente con cedula : "+ced+" se modifico correctamente")
            else:
                msg.setText("Campos vacios")
        else :
            msg.setText("El cliente con cedula : "+ced+" no se encuentra registrado")
        x=msg.exec_()   
        self.limpiar() 

    def limpiar(self):
        self.lineEdit_cedula.clear()
        self.lineEdit_nombre.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_correo.clear()
        self.lineEdit_direccion.clear()
        self.lineEdit_fecha.clear()    
         
        
        
          

    def verifica_cedula(self,ced):
        sql="select * from clientes where cedula ='"+ced+"';"
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
        msg.setWindowTitle("Modificar cliente")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_cedula(ced):


            self.cursor.execute("select nombre,telefono,correo,direccion,fecha_nacimiento from clientes where cedula='"+ced+"';")  
            a=self.cursor.fetchone()
            nombre,telefono,correo,direccion,fecha_nacimiento=" "," "," "," "," "
            c=[nombre,telefono,correo,direccion,fecha_nacimiento]
            for i in range(len(a)):
                c[i]=a[i]  

            self.lineEdit_nombre.setText(str(c[0]))
            self.lineEdit_telefono.setText(str(c[1]))
            self.lineEdit_correo.setText(str(c[2]))
            self.lineEdit_direccion.setText(str(c[3]))   
            self.lineEdit_fecha.setText(str(c[4]))
            self.lineEdit_telefono.setValidator(QtGui.QDoubleValidator())    
        else:
            msg.setText("El cliente con cedula : "+ced+" no se encuentra registrado")
            x=msg.exec_() 

        
    def cancelar(self):
        self.close()    




if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Modifica_cliente()
    window.show()
    sys.exit(app.exec_())        