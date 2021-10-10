import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import psycopg2 #importar la libreria 

qtCreatorFile = "inter_consultar_cliente.ui" # Nombre del archivo que creamos en Qt dessigener en nuestro caso calculadora_suma.iu.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class Consultar_cliente(QtWidgets.QMainWindow, Ui_MainWindow):# nobre de la clase como tal siempre igual
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
        self.tabla_clientes=QTableWidget(self)      
        self.inicio_tabla_clientes()          
        self.btn_consultar.clicked.connect(self.consultar) #evento de registrar
        self.btn_limpiar.clicked.connect(self.limpiar) #evento de cncelar

    def consultar(self):
        msg=QMessageBox() 
        msg.setWindowTitle("Consultar cliente")
        msg.setIcon(QMessageBox.Information) 
 
        b1=True
        ced=self.lineEdit_cedula.text()
        if not self.lineEdit_cedula.text():
            b1=False
        if b1:
            if self.verifica_cedula(ced):
                self.tabla_clientes.clear()
                self.cursor.execute("select * from clientes where cedula ='"+ced+"';")  
                mio= self.cursor.fetchall()
                self.inicio_tabla_clientes()
                self.datos_tabla_clientes(self.tabla_clientes,mio)
                msg.setText("Consulta exitosa")
            else:
                msg.setText("El cliente con cédula : "+ced+" no se encuentra registrado")
        else:
            msg.setText("Campos vacios")
        x=msg.exec_()    


    def verifica_cedula(self,ced):
        sql="select * from clientes where cedula ='"+ced+"';"
        self.cursor.execute(sql)
        a=self.cursor.fetchall()
        self.conn.commit()
        if len(a)>=1 :
            return True
        else:
            return False
 
    def inicio_tabla_clientes(self):
        self.tabla_clientes.setColumnCount(6)
        nombreColumnas = ( "Cedula","Nombre","Telefono", "Correo","Direccion","Fecha de nacimiento")
        self.tabla_clientes.setHorizontalHeaderLabels(nombreColumnas)
        for i in range(5):
            self.tabla_clientes.setColumnWidth(i,70) 
        self.tabla_clientes.setGeometry(50,200,691,150)
        self.iniciarTabla(self.tabla_clientes)     

    def datos_tabla_clientes(self,tabla,datillos):
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
          
    def limpiar(self):
        self.tabla_clientes.clear()
        self.inicio_tabla_clientes()
        self.lineEdit_cedula.clear()  

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window =Consultar_cliente()
    window.show()
    sys.exit(app.exec_())   