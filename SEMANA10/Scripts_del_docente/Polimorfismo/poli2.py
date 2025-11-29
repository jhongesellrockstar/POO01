class Perro:
    def hablar(self):
        print('Guau, Guau')
        
class Gato:
    def hablar(self):
        print('Miau, Miau')
        
class Vaca:
    def hablar(self):
        print('Muuu, Muuu')
        
def llama_hablar(x):
    x.hablar()
        
'''p=Perro()
#p.hablar()
g=Gato()
#g.hablar()
v=Vaca()
#v.hablar()'''

'''llama_hablar(p)
llama_hablar(g)
llama_hablar(v)'''

'''llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())'''

lista=[Perro(),Gato(),Vaca()]
for animal in lista:
    animal.hablar()

