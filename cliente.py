class Cliente:
    # clase cliente permite crear objetos de tipo cliente 
    def __init__(self,cedula,nombre,telefono,correo,direccion,fecha_nac):#constructtor de la clase cliente 
        self.cedula=cedula
        self.nombre=nombre
        self.telefono=telefono
        self.correo=correo
        self.direccion=direccion
        self.fecha_nac=fecha_nac
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

    def obtener_fecha_nac(self):
        return self.fecha_nac         
    #FIN GETTERS___________________________________________________________________________

    #SETTERS_______________________________________________________________________________
    def cambiar_nombre(self,nombre):#metodo para cambiar el nombre del cliente 
        self.nombre =nombre
    
    def cambiar_telefono(self,tel):
        self.telefono =tel

    def cambiar_correo(self,correo):
        self.correo=correo

    def cambiar_direccio(self,direccion):
        self.direccion=direccion

    def cambiar_fecha_nac(self,fecha):
        self.fecha_nac=fecha 
    #FIN SETTERS_____________________________________________________________________________

    def obtener_info(self):
        ra= (str(self.cedula)+" , "+str(self.nombre)+ " , "+str(self.telefono)+" , "+str(self.direccion)+
               " , "+str(self.correo)+" , "+str(self.fecha_nac))
        return ra  
             
        """
        
        
clie=Cliente("1004199","Hernando andres","2030404","hernandopanto85@gmail.com","manzanda d casa 23","12-34-5000")
print(clie.obtener_info())
clie.cambiar_nombre("Daniel tobar")
print(clie.obtener_info())
"""
                                