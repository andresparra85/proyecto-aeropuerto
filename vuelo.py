from hangar import Hangar
class Vuelo:
    #clase vuelo me permitira crear objetos de tipo vuelo

    def __init__(self,id_vuelo,origen,destino,fecha,hora_salida,hangar,avion,cantidad_puestos,precio):#constructor de hangar
        self.id_vuelo=id_vuelo
        self.origen=origen
        self.destino=destino
        self.fecha=fecha
        self.hora_salida=hora_salida
        self.hangar=hangar
        self.avion=avion
        self.cantidad_puestos=cantidad_puestos
        self.precio=precio
        self.estado="En proceso"

    #GETTERS_____________________________________________

    def obtener_id_vuelo(self):
        return self.id_vuelo

    def obtener_origen(self):
        return self.origen

    def obtener_destino(self):
        return self.destino

    def obtener_fecha(self):
        return self.fecha

    def obtener_hora_salida(self):
        return self.hora_salida

    def obtener_hangar(self):
        return self.hangar

    def obtener_avion(self):
        return self.avion

    def obtener_cantidad_puestos(self):
        return self.cantidad_puestos  

    def obtener_precio(self):
        return self.precio

    def obtener_estado(self):
        return self.estado  
    

     #SETTERS_______________________________________________________________________________                       
    
    def cambiar_origen(self,origen):#
        self.origen=origen
        
    def cambiar_destino(self,destino):#
        self.destino=destino

    def cambiar_fecha(self,fecha):#
        self.fecha=fecha

    def cambiar_hora_salida(self,hora):#
        self.hora_salida=hora
        
    def cambiar_hangar(self,hangar):#
        self.hangar=hangar

    def cambiar_avion(self,avion):#
        self.avion=avion        

    def cambiar_cant_puestos(self,puestos):#
        self.cantidad_puestos=self.cantidad_puestos-puestos
        
    def cambiar_precio(self,precio):#
        self.precio=precio

    def cambiar_estado(self,variable):#
        self.estado=variable

    #FIN SETTERS___________________________________________________________________________
    def obtener_info(self):
        return  (str(self.id_vuelo)+" , "+
                self.origen+" , "+
                self.destino+" , "+
                self.fecha+" , "+
                self.hora_salida+" , "+
                self.hangar+" , "+
                self.avion+" , "+
                str(self.cantidad_puestos)+" , "+
                str(self.precio)+" , "+
                self.estado)

    def __str__(self):
        return  (str(self.id_vuelo)+" , "+
                self.origen+" , "+
                self.destino+" , "+
                self.fecha+" , "+
                self.hora_salida+" , "+
                self.hangar+" , "+
                self.avion+" , "+
                str(self.cantidad_puestos)+" , "+
                str(self.precio)+" , "+
                self.estado)            
"""
              
hanga=Hangar("133","34")
hanga1=Hangar("23","345")
hanga.cambiar_estado("lleno")
vuelo=vuelo("100","Pasto","cali","22-10-2021","5 pm",hanga,"avionetica ",60,125367.67)
print(vuelo.obtener_info())
vuelo.cambiar_origen("bogota")
vuelo.cambiar_estado("en curso")
print(vuelo.obtener_info())
vuelo.cambiar_hangar(hanga1)
vuelo.cambiar_estado("en tierra destino")
print(vuelo.obtener_info())
"""  