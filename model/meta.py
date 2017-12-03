import uuid
class Meta:

    def __init__(self,nombre,valor):
        self.valor=valor
        self.nombre=nombre
        id=uuid.uid4()
    def getValor(self):
        return self.valor
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
