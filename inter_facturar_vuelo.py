import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from vuelo import Vuelo
from PyQt5.QtWidgets import*
from cliente import Cliente
import psycopg2 #importar la libreria 
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner

qtCreatorFile = "inter_facturar_vuelo.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja

class Factura_vuelo(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
    def __init__(self):#metodo constructor 
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.b=True
        self.conn=psycopg2.connect(
        host="localhost",
        database ="aeropuertodb",
        user= "postgres",
        password="postgres1" )
        print("Coneccion exitosa")
        self.cursor=self.conn.cursor()

        self.setupUi(self)# hasta aqui metodos de inicializacion siemore van no los borre
        
        self.lineEdit_num_tiquetes.setValidator(QtGui.QDoubleValidator())
        self.btn_facturar.clicked.connect(self.facturar) #evento de facturar
        self.btn_cancelar.clicked.connect(self.cancelar) #evento de cncelar
        self.btn_imprimir.clicked.connect(self.imprime) #evento de cncelar
        self.tabla_vuelos=QTableWidget(self)#Creacion de la tabla  
        self.todos()
     
    # funcion para boton registrar    
    def todos(self):
        self.tabla_vuelos.clear()
        self.cursor.execute("select * from vuelos where estado ='En Proceso' ;")  
        mio= self.cursor.fetchall()
        self.inicio_tabla_vuelos()#metodo para inicializar la tabla ejecucion
        self.datos_tabla_vuelos(self.tabla_vuelos,mio)
        self.tabla_vuelos.show()  
            
        
    

    def verifica_cedula(self,ced):
        sql="select * from clientes where cedula ='"+ced+"';"
        self.cursor.execute(sql)#
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False
           
              

      
    # funcion para boton finalizar    
    def facturar(self):
        #sacamos en variables toda la informacion
        msg=QMessageBox()
        msg.setWindowTitle("Facturar vuelos")
        try:
            num=self.lineEdit_num_tiquetes.text()
            ced=self.lineEdit_cliente.text()
            if self.verifica_cedula(ced) and int(num) >=0:
                row = self.tabla_vuelos.currentRow()
                item = self.tabla_vuelos.item(row,0)
                t=None
                if item:
                    t=item.text()               
                if t:
                    msg1=QMessageBox()
                    msg1.setWindowTitle("Factura vuelos")
                    msg1.setIcon(QMessageBox.Information)
                    msg1.setText("La facturacion se hizo correctamente")
                    y=msg1.exec_()
                    self.genera(ced,t) 
                    self.actualiza_puestos(num,t)
                    self.lineEdit_num_tiquetes.clear()
                    self.lineEdit_cliente.clear()
                else:
                    msg1=QMessageBox()
                    msg1.setWindowTitle("Factura vuelos")
                    msg1.setIcon(QMessageBox.Information)
                    msg1.setText("No hay vuelos por el momento")
                    y=msg1.exec_()           
            else:
                msg1=QMessageBox()
                msg1.setWindowTitle("Factura vuelos")
                msg1.setIcon(QMessageBox.Information)
                msg1.setText("el cliente con cedula : "+ced+" No se encuentra registrado ")
                y=msg1.exec_()
        except:

            msg.setIcon(QMessageBox.Information)
            msg.setText("faltan parametros ")
            y=msg.exec_()  
        

    def cancelar(self):
        self.close()

    def imprime(self):
        msg1=QMessageBox()
        msg1.setWindowTitle("imprimiendo reporte")
        msg1.setIcon(QMessageBox.Information)
        msg1.setText("el Reporte esta siendo impreso en estos mementos..... ")
        y=msg1.exec_()    
        self.textEdit.clear()

    def genera(self,ced,vue):
        self.cursor.execute("select id_vuelo,origen,destino,fecha,hora,hangar,avion,cant_puestos,precio from vuelos where id_vuelo='"+vue+"';")  
        a=self.cursor.fetchone()
        id_vuelo,origen,destino,fecha,hora_salida,hangar,avion,cantidad_puestos,precio=" "," "," "," "," "," "," "," "," "
        c=[id_vuelo,origen,destino,fecha,hora_salida,hangar,avion,cantidad_puestos,precio]
        for i in range(len(a)):
            c[i]=a[i]
               
        vue=Vuelo(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8])
        self.cursor.execute("select cedula,nombre,telefono from clientes where cedula='"+ced+"';")  
        a1=self.cursor.fetchone()
        clie=Cliente(a1[0],a1[1],a1[2],None,None,None)
        
        a=("*****************F-A-C-T-U-R-A*******************"+"\n "+
          "Cedula: "+str(clie.cedula)+"\n "+
          "Nombre: "+str(clie.nombre)+"\n "+ 
          "Telefono: "+str(clie.telefono)+"\n "+
          "ORIGEN : "+vue.origen+"\n "+
            "Destino : "+vue.destino+" , "+"\n "+
            "Fecha de salida :" + vue.fecha+"\n "+
            "Hora de salida: "+vue.hora_salida+"\n "+
            "Hangar : "+vue.hangar+"\n "+
            "Avion : "+vue.avion+"\n "+
            "Precio :" +str(vue.precio) +"\n "+
            "Cantidad de tiquetes: "+self.lineEdit_num_tiquetes.text()+"\n "+
            "Pago :"+str(int(vue.precio)*int(self.lineEdit_num_tiquetes.text()))+"\n "+
            "Gracias por su compra ....ATM: Aeropuerto el Campanero")
        self.textEdit.setText(a)

    def actualiza_puestos(self,num,vue):
        self.cursor.execute("select cant_puestos from vuelos where id_vuelo='"+vue+"';")  
        a=self.cursor.fetchone()
        t=""
        for i in a:
            if i=="(" or i=="'":
                pass
            elif i ==",":
                break 
            else:
                t+=str(i) 
        
        a1=int(t)-int(num)
        self.cursor.execute("update vuelos set cant_puestos='"+str(a1)+"' where id_vuelo='"+vue+"';")  
        self.conn.commit()
        self.todos()

    def inicio_tabla_vuelos(self):
        self.tabla_vuelos.setColumnCount(9)
        nombreColumnas = ( "id_vuelo","Origen","Destino","fecha", "hora","hangar","avion","# puestos","precio")
        self.tabla_vuelos.setHorizontalHeaderLabels(nombreColumnas)
        for i in range(7):
            self.tabla_vuelos.setColumnWidth(i,70) 
        self.tabla_vuelos.setGeometry(200,50,760,100)
        self.iniciarTabla(self.tabla_vuelos)     

    def datos_tabla_vuelos(self,tabla,datillos):
        tabla.clearContents()
        row = 0
        for endian in datillos:
            tabla.setRowCount(row+1)
            tabla.setItem(row, 0, QTableWidgetItem(endian[0]))
            tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
            tabla.setItem(row, 4, QTableWidgetItem(endian[4]))
            tabla.setItem(row, 5, QTableWidgetItem(endian[5]))
            tabla.setItem(row, 6, QTableWidgetItem(endian[6]))
            tabla.setItem(row, 7, QTableWidgetItem(endian[7]))
            tabla.setItem(row, 8, QTableWidgetItem(endian[8]))
            row += 1

    def iniciarTabla(self,tabla1):
            tabla1.setStyleSheet('background-color: rgb(255, 255, 255);')
            tabla1.setEditTriggers(QAbstractItemView.NoEditTriggers)# Deshabilitar edición
            tabla1.setDragDropOverwriteMode(False)# Deshabilitar el comportamiento de arrastrar y soltar
            tabla1.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleccionar toda la fila
            tabla1.setSelectionMode(QAbstractItemView.SingleSelection)# Seleccionar una fila a la vez
            tabla1.setTextElideMode(Qt.ElideRight)# Qt.ElideNone 
            tabla1.setWordWrap(False) # Establecer el ajuste de palabras del texto
            tabla1.setSortingEnabled(False)# Deshabilitar clasificación
            tabla1.setRowCount(0)
            tabla1.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                            Qt.AlignCenter)# Alineación del texto del encabezado
            tabla1.horizontalHeader().setHighlightSections(False)# Deshabilitar resaltado del texto del encabezado al seleccionar una fila
            tabla1.horizontalHeader().setStretchLastSection(True) # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
            tabla1.verticalHeader().setVisible(False)# Ocultar encabezado vertical
            tabla1.setAlternatingRowColors(True)# Dibujar el fondo usando colores alternados
            tabla1.verticalHeader().setDefaultSectionSize(20)# Establecer altura de las filas
          
       
   

        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Factura_vuelo()
    window.show()
    sys.exit(app.exec_())
    
