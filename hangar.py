class Hangar:
    #clase hangar me permitira crear objetos de tipo hangar
    def __init__(self,id_hangar,area):#constructor de hangar
        self.id_hangar=id_hangar
        self.area=area
        self.estado="Libre"

    #GETTERS_________________________________________________________________________________
    def obtener_id_hangar(self):#
        return self.id_hangar

    def obtener_area(self):#
        return self.area+" m2"

    def obtener_estado(self):#
        return self.estado

    #FIN GETTERS___________________________________________________________________________

    #SETTERS_______________________________________________________________________________                       
    
    def cambiar_id_hangar(self,id):#
        self.id_hangar=id
        
    def cambiar_area(self,area):#
        self.area=area

    def cambiar_estado(self,variable):#
        self.estado=variable

    #FIN SETTERS___________________________________________________________________________
    
    def __str__(self):
        return self.id_hangar+ " , " + self.obtener_area() +" , " + self.estado

     
    def obtener_info(self):
        return self.id_hangar+ " , " + self.obtener_area() +" , " + self.estado    



        
        

        """
han=Hangar("100","50")     

print(han.info_hangar())

han.cambiar_estado("Ocupado")
han.cambiar_area("400")
print(han.info_hangar())

han.cambiar_estado("Libre")
print(han.info_hangar())
"""