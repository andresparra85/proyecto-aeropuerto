class Empleado:

    def __init__(self,cedula,nombre,telefono,correo,direccion,edad,sueldo,fecha_ingreso):#constructor clase empleado
        self.cedula=cedula
        self.nombre=nombre
        self.telefono=telefono
        self.correo=correo
        self.direccion=direccion
        self.edad=edad
        self.sueldo=sueldo
        self.fecha_ingreso=fecha_ingreso
        self.estado="Activo" 
    #GETTERS_________________________________________________________________________________
    def obtener_cedula(self):#metodo que retorna la cedula del cliente 
        return self.cedula

    def obtener_nombre(self):#metodo que retorna el nombre del cliente
        return self.nombre 

    def obtener_telefono(self):
        return self.telefono

    def obtener_correo(self):
        return self.correo

    def obtener_direccion(self):
        return self.direccion

    def obtener_edad(self):
        return self.edad

    def obtener_sueldo(self):
        return self.sueldo

    def obtener_fecha_ingreso(self):
        return self.fecha_ingreso    

    def obtener_estado(self):
        return self.estado

    #FIN GETTERS___________________________________________________________________________

    #SETTERS_______________________________________________________________________________
    
    def cambiar_nombre(self,nombre):
        self.nombre =nombre 

    def cambiar_telefono(self,telefono):
        self.telefono =telefono

    def cambiar_correo(self,correo):
        self.correo =correo

    def cambiar_direccion(self,direccion):
        self.direccion =direccion

    def cambiar_edad(self,edad):
        self.edad =edad

    def cambiar_sueldo(self,sueldo):
        self.sueldo =sueldo

    def cambiar_fecha_ingreso(self,fecha_ingreso):
        self.fecha_ingreso =fecha_ingreso

    def cambiar_estado(self,variable):
        self.estado =variable
    #FIN SETTERS_____________________________________________________________________________

    def obtener_info(self):
        ra= (str(self.cedula)+" , "+str(self.nombre)+ " , "+str(self.telefono)+" , "+str(self.correo)+
        " , "+str(self.direccion)+" , "+str(self.edad)+" , "+str(self.sueldo)+" , "+str(self.fecha_ingreso)
        +" , "+str(self.estado))
        return ra   
"""
            

emple=Empleado("123123123","Daniel Tobar","23172818","danielt@gmail.com","calle 23 carrera 15","30","10000000","10-02-2021")
print(emple.obtener_info())
emple.cambiar_nombre("Andres")
print(emple.obtener_info())
emple.cambiar_estado("Inactivo")
print(emple.obtener_info())

"""