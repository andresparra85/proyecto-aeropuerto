import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "inter_registrar_cliente.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Registre_clien(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
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
        
        self.setupUi(self)# hasta aqui metodos de inicializacion siemore van no los borre
        self.texto()#metodo para agregar valores por defecto a los qlineedit
        self.agrega_anios()#metodo para gregar valores a las listas desplegables
        self.btn_registrar.clicked.connect(self.registrar) #evento de registrar
        self.lineEdit_telefono.setValidator(QtGui.QDoubleValidator())
        self.btn_cancelar.clicked.connect(self.cancelar) #evento de cncelar
    def verifica_cedula(self,ced):
        sql="select * from clientes where cedula ='"+ced+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False    

    # funcion para boton registrar    
    def registrar(self):
        b1=True
        #sacamos en variables toda la informacion
        ced=self.lineEdit_cedula.text()
        if not self.lineEdit_cedula.text():
            b1=False
        nom=self.lineEdit_nombre.text()
        if not self.lineEdit_nombre.text():
            b1=False
        correo=self.lineEdit_correo.text()
        dirc=self.lineEdit_direccion.text()
        fecha=self.comboBox_dia.currentText()+"/"+self.comboBox_mes.currentText()+"/"+self.comboBox_anio.currentText()
        tel=self.lineEdit_telefono.text()
        if not self.lineEdit_telefono.text():
            b1=False
        
        #creamos la ventana desplegable
        msg=QMessageBox()
        # ponemos nombre a la ventana 
        msg.setWindowTitle("Registro de Clientes")
        b=False
        # aqui verificamos si el cliente existe 
        if self.verifica_cedula(ced) is False:
            msg.setIcon(QMessageBox.Information)
            msg.setText("El Cliente: " +nom +" con Cedula : " + ced+ 
                " se registro satisfactoriamente")
            self.cursor.execute("INSERT INTO clientes VALUES " \
            "('"+ced+"','"+nom+"','"+correo+"','"+dirc+"','"+fecha+"','"+tel+"')")       
            self.conn.commit()
            
        elif b1:
            msg.setIcon(QMessageBox.Information)
            msg.setText("La cedula:  " + ced+ 
                " ya se encuentra registrada")
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Campos Obligatorios Vacios")


        x=msg.exec_()    
        self.limpiar()
        
        
    def texto(self):
        self.lineEdit_cedula.setPlaceholderText("Digite la cedula ")
        self.lineEdit_nombre.setPlaceholderText("Digite el nombre completo ")
        self.lineEdit_direccion.setPlaceholderText("Digite la direccion  ")
        self.lineEdit_telefono.setPlaceholderText("Digite el telefono ")
        self.lineEdit_correo.setPlaceholderText("Digite el correo electronico ")

    def limpiar(self):
        self.lineEdit_cedula.clear()
        self.lineEdit_nombre.clear()
        self.lineEdit_direccion.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_correo.clear()    
    
    def agrega_anios(self):
        i=2021
        while i>1900:
            self.comboBox_anio.addItem(str(i))
            i=i-1

    def cancelar(self):
        if self.b:
            self.conn.close()
        self.close()



if __name__ == "__main__":
    
    app =  QtWidgets.QApplication(sys.argv)
    
    window =Registre_clien()
    window.show()
    sys.exit(app.exec_())
        

    
     