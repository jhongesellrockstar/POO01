# Problema03
class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = [] # lista de nombres de hijos

    def __str__(self):
        return f'Familia[Padre: {self.padre}, Madre: {self.madre}, Hijos: {", ".join(self.hijos)}]'
    
familia1 = Familia('Carlos', 'Ana', [])
familia1.hijos.append('Luis')
familia1.hijos.append('Maria')
print(familia1)


    