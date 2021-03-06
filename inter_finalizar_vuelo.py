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
        self.tabla_vuelos=QTableWidget(self)#Creacion de la tabla                 
        self.agrega()
        self.btn_finalizar.clicked.connect(self.finalizar) #evento de registrar
        self.btn_cancelar.clicked.connect(self.cancelar) #evento de cncelar
    #para las tablas      
    def agrega(self):
        self.tabla_vuelos.clear()
        self.cursor.execute("select * from vuelos where estado ='En Proceso' ;")  
        mio= self.cursor.fetchall()
        self.inicio_tabla_vuelos()#metodo para inicializar la tabla ejecucion
        self.datos_tabla_vuelos(self.tabla_vuelos,mio)
        self.tabla_vuelos.show()  
    # funcion para boton finalizar    
    def finalizar(self):
        #sacamos en variables toda la informacion
        row = self.tabla_vuelos.currentRow()
        item = self.tabla_vuelos.item(row,0)
        t=None
        if item:
            t=item.text()
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
        self.tabla_vuelos.clear()    
        self.agrega()

    def inicio_tabla_vuelos(self):
        self.tabla_vuelos.setColumnCount(9)
        nombreColumnas = ( "id_vuelo","Origen","Destino","fecha", "hora","hangar","avion","# puestos","precio")
        self.tabla_vuelos.setHorizontalHeaderLabels(nombreColumnas)
        for i in range(7):
            self.tabla_vuelos.setColumnWidth(i,70) 
        self.tabla_vuelos.setGeometry(50,50,691,150)
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
            tabla1.setEditTriggers(QAbstractItemView.NoEditTriggers)# Deshabilitar edici??n
            tabla1.setDragDropOverwriteMode(False)# Deshabilitar el comportamiento de arrastrar y soltar
            tabla1.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleccionar toda la fila
            tabla1.setSelectionMode(QAbstractItemView.SingleSelection)# Seleccionar una fila a la vez
            tabla1.setTextElideMode(Qt.ElideRight)# Qt.ElideNone 
            tabla1.setWordWrap(False) # Establecer el ajuste de palabras del texto
            tabla1.setSortingEnabled(False)# Deshabilitar clasificaci??n
            tabla1.setRowCount(0)
            tabla1.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                            Qt.AlignCenter)# Alineaci??n del texto del encabezado
            tabla1.horizontalHeader().setHighlightSections(False)# Deshabilitar resaltado del texto del encabezado al seleccionar una fila
            tabla1.horizontalHeader().setStretchLastSection(True) # Hacer que la ??ltima secci??n visible del encabezado ocupa todo el espacio disponible
            tabla1.verticalHeader().setVisible(False)# Ocultar encabezado vertical
            tabla1.setAlternatingRowColors(True)# Dibujar el fondo usando colores alternados
            tabla1.verticalHeader().setDefaultSectionSize(20)# Establecer altura de las filas
          
    def cancelar(self):
        self.close()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Finaliza_vue()
    window.show()
    sys.exit(app.exec_())