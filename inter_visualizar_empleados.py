import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 
#Librerias elementales para poder correr nuestros archivos creados en el QT dessigner
qtCreatorFile = "inter_visualizar_empleados.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)# nose que hace pero siempre va jajajaja
class visualiza_empleados(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal seiempre igual
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
        self.tabla_empleados=QTableWidget(self)#Creacion de la tabla       
        self.inicio_tabla_empleados()  
        self.visualizar()        
        self.btn_cerrar.clicked.connect(self.clos) #evento de cncelar

    def visualizar(self):
      
        self.tabla_empleados.clear()
        self.cursor.execute("select * from empleados;")  
        mio= self.cursor.fetchall()
        print(len(mio))
        if len(mio)<0:
            msg=QMessageBox()
            msg.setWindowTitle("visualizar empleados")
            msg.setIcon(QMessageBox.Information)
            msg.setText("NO HAY EMPLEADOS REGISTRADOS")
            x=msg.exec_()     
        self.inicio_tabla_empleados()#metodo para inicializar la tabla ejecucion
        self.datos_tabla_empleados(self.tabla_empleados,mio)
         

    
                       
    def inicio_tabla_empleados(self):
        self.tabla_empleados.setColumnCount(9)
        nombreColumnas = ( "Cedula","Nombre","Telefono", "Correo","Direccion","Edad","Saldo","Fecha ingreso","Estado")
        self.tabla_empleados.setHorizontalHeaderLabels(nombreColumnas)
        for i in range(7):
            self.tabla_empleados.setColumnWidth(i,70) 
        self.tabla_empleados.setGeometry(50,100,691,250)
        self.iniciarTabla(self.tabla_empleados)     

    def datos_tabla_empleados(self,tabla,datillos):
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
    
    def clos(self):
        self.close()
     
          
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =visualiza_empleados()
    window.show()
    sys.exit(app.exec_())   
