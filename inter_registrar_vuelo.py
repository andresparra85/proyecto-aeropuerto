import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "inter_registrar_vuelo.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Registre_vuelo(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
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
        self.btn_cancelar.clicked.connect(self.cancelar) #evento de cncelar
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.todos()
        self.lineEdit_cant_puestos.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_precio_tickets.setValidator(QtGui.QDoubleValidator())
       
    # funcion para boton registrar    
    
        
    def m(self):# funcion para registrar un nuevo id del vuelo
        self.cursor.execute("select * from id ;")
        hanga = self.cursor.fetchall()
        for ha in hanga:
            palabra=""
            for i in ha:
                if i=="(" or i==")" or i==",":
                    pass
                else:
                    palabra+=str(i)                      
        a=int(palabra)+10
        self.cursor.execute("update id set id= '"+str(a)+"' ;")
        self.conn.commit ()
        return a
       
    def verifica_hangar(self,id):
        sql="select * from hangares where id_hangar='"+id+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        if len(a)>0:
            return True
        else:
            return False   

    def todos(self):
        self.comboBox.clear()
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
        
    def registrar(self):

        msg=QMessageBox()
        msg.setWindowTitle("Facturar vuelos")
        try:
            b=True
            #sacamos en variables toda la informacion
            origen=self.lineEdit_origen.text()
            if self.lineEdit_origen.text()=="":
                b=False
            destino=self.lineEdit_destino.text()
            hora=self.lineEdit_hr_salida.text()
            hangar=self.comboBox.currentText()
            fecha=self.comboBox_dia.currentText()+"/"+self.comboBox_mes.currentText()+"/"+self.comboBox_anio.currentText()
            avion=self.lineEdit_avion.text()
            can_puestos=self.lineEdit_cant_puestos.text()
            precio=self.lineEdit_precio_tickets.text()
            #creamos el vuelo con la informacion subministrada        
            #creamos la ventana desplegable
            msg=QMessageBox()
            # ponemos nombre a la ventana 
            msg.setWindowTitle("Registro de Vuelos")
            # aqui verificamos si el cliente existe 
            if self.verifica_hangar(str(hangar)) and b:
                msg.setIcon(QMessageBox.Information)
                msg.setText("El vuelo : " +str(self.m()) +" con Origen : " + origen+ 
                    " y destino : "+destino+ " se registro satisfactoriamente")
                #modificar estado del hangar :
                self.cursor.execute("update hangares set estado ='Ocupado' where id_hangar ='"+hangar+"';")
                self.conn.commit ()
                self.todos()

                self.cursor.execute("INSERT INTO vuelos VALUES " \
                "('"+str(self.m())+"','"+origen+"','"+destino+"','"+fecha+"','"+hora+"','"+hangar+"','"+avion+"','"+can_puestos+"','"+precio+"','En Proceso');")       
             
                self.conn.commit()
            elif b:
                msg.setIcon(QMessageBox.Information)
                msg.setText("Campos vacios")

            else:
                msg.setIcon(QMessageBox.Information)
                msg.setText("NO HAY HANGARES DISPONIBLES")

            x=msg.exec_()    
            self.limpiar()
  
        
        except:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Parametros vacios o no se esperaban ese tipo de parametros ")
            y=msg.exec_()


  
    def texto(self):
        self.lineEdit_origen.setPlaceholderText("Digite el origen ")
        self.lineEdit_destino.setPlaceholderText("Digite el Destino ")
        self.lineEdit_avion.setPlaceholderText("Digite el avion  ")
        self.lineEdit_precio_tickets.setPlaceholderText("Digite el precio ")
        self.lineEdit_cant_puestos.setPlaceholderText("Digite el numero de puestos ")
        self.lineEdit_hr_salida.setPlaceholderText("Digite el numero de puestos ")

    def limpiar(self):
        self.lineEdit_origen.clear()
        self.lineEdit_destino.clear()
        self.lineEdit_avion.clear()
        self.lineEdit_precio_tickets.clear()
        self.lineEdit_cant_puestos.clear()
        self.lineEdit_hr_salida.clear()
       
    def agrega_anios(self):
        i=2021
        while i>1900:
            self.comboBox_anio.addItem(str(i))
            i=i-1

    def cancelar(self):
        self.close()


if __name__ == "__main__":

    app =  QtWidgets.QApplication(sys.argv)
    window =Registre_vuelo()
    window.show()
    sys.exit(app.exec_())
        
    