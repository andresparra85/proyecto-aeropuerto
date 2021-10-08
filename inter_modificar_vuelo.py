import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
from functools import partial
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner
qtCreatorFile = "inter_modificar_vuelo.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja
class Modifica_vuelo(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
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
        self.lineEdit_id_vuelo.returnPressed.connect(self.genera_datos)
        self.btn_modificar.clicked.connect(self.modifica_datos) 
        self.btn_cancelar.clicked.connect(self.cancelar)         

    def modifica_datos(self):
        id_vuelo=self.lineEdit_id_vuelo.text()
        b=True
        if self.lineEdit_origen.text()=="":
            b=False
        if self.lineEdit_destino.text()=="":
            b=False    
            if self.lineEdit_origen.text()=="":
                b=False
        origen=self.lineEdit_origen.text()        
        destino=self.lineEdit_destino.text()
        hora=self.lineEdit_hora.text()
        hangar=self.comboBox.currentText()
        fecha=self.lineEdit_fecha.text()
        avion=self.lineEdit_avion.text()
        can_puestos=self.lineEdit_cant_puestos.text()
        precio=self.lineEdit_precio_tickets.text()
        estado=self.comboBox_estado.currentText()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar vuelo")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_vuelo(id_vuelo):
            if b:
                if estado=='En Proceso':
                   self.cursor.execute("update hangares set estado ='Ocupado' where id_hangar ='"+hangar+"';")
                else:
                    self.cursor.execute("update hangares set estado ='Libre' where id_hangar ='"+hangar+"';")

                self.conn.commit ()
                self.cursor.execute("update vuelos set origen ='"+origen+"',destino='"+destino+"',fecha='"+fecha+"',hora='"+hora+"',hangar='"+hangar+"',avion='"+avion+"',cant_puestos = '"+can_puestos+"',precio= '"+precio+"',estado='"+estado+"'  where id_vuelo='"+id_vuelo+"';")
                self.conn.commit()
                msg.setText("El vuelo con id_vuelo : "+id_vuelo+" se modifico correctamente")
            else:
                msg.setText("Campos vacios")
        else :
            msg.setText("El vuelo con id_vuelo : "+id_vuelo+" no se encuentra registrado")
        x=msg.exec_()   
        self.limpiar() 

    def limpiar(self):
        self.lineEdit_id_vuelo.clear()
        self.lineEdit_origen.clear()        
        self.lineEdit_destino.clear()
        self.lineEdit_hora.clear()
        self.comboBox.clear()
        self.lineEdit_fecha.clear()
        self.lineEdit_avion.clear()
        self.lineEdit_cant_puestos.clear()
        self.lineEdit_precio_tickets.clear()
        
         
        
    def todos(self):
        #self.comboBox.clear()
        self.cursor.execute("SELECT id_hangar FROM hangares where estado ='Libre' ;")
        hanga = self.cursor.fetchall()
        for ha in hanga:
            palabra=""
            for i in ha:
                if i=="(" or i==")" or i==",":
                    pass
                else:
                    palabra+=str(i)
            self.comboBox.addItem(palabra)        
          

    def verifica_vuelo(self,id_vuelo):
        sql="select * from vuelos where id_vuelo ='"+id_vuelo+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False
                       
    def genera_datos(self):
        self.comboBox.clear()
        id_vuelo=self.lineEdit_id_vuelo.text()
        msg=QMessageBox() 
        msg.setWindowTitle("Modificar empleado")
        msg.setIcon(QMessageBox.Information) 
        if self.verifica_vuelo(id_vuelo):
            self.cursor.execute("select origen,destino,fecha,hora,hangar,avion,cant_puestos,precio,estado from vuelos where id_vuelo='"+id_vuelo+"';")  
            a=self.cursor.fetchone()
            origen,destino,fecha,hora_salida,hangar,avion,cantidad_puestos,precio,estado=" "," "," "," "," "," "," "," "," "
            c=[origen,destino,fecha,hora_salida,hangar,avion,cantidad_puestos,precio,estado]
            for i in range(len(a)):
               c[i]=a[i]        
            self.lineEdit_origen.setText(str(c[0]))
            self.lineEdit_destino.setText(str(c[1]))
            self.lineEdit_fecha.setText(str(c[2]))
            self.lineEdit_hora.setText(str(c[3]))   
            self.lineEdit_avion.setText(str(c[5]))
            self.lineEdit_cant_puestos.setText(str(c[6]))
            self.lineEdit_precio_tickets.setText(str(c[7]))
            if str(c[8])=='En Proceso':
                self.comboBox_estado.setCurrentIndex(0)  
                self.comboBox.addItem(str(c[4]))
                
            else:
                self.comboBox_estado.setCurrentIndex(1)
            self.todos() 
            self.lineEdit_cant_puestos.setValidator(QtGui.QDoubleValidator())
            self.lineEdit_precio_tickets.setValidator(QtGui.QDoubleValidator())    
        else:
            msg.setText("el vuelo con id : "+id_vuelo+" no se encuentra registrado")
            x=msg.exec_() 

        
    def cancelar(self):
        self.close()    




if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Modifica_vuelo()
    window.show()
    sys.exit(app.exec_())        