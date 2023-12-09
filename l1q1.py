class Stack:
  def __init__(self,pilha):
    self.relacao={"endrick":"new balance","messi":"adidas","cr7":"nike","neymar":"puma"}
    self.camisas_encontradas=set()
    self.elementos=pilha.split("-")
    self.aprovados=[]
    
  def verificar_pilha(self):
    for elemento in self.elementos:
      if self.camisa(elemento):
        self.camisas_encontradas.add(elemento)
      elif self.chuteira(elemento):
        camisa_corresp = self.encontrar_camisa(elemento)
        if camisa_corresp is False:
          return "Incorreto"
    for aprovado in self.aprovados:
      self.elementos.remove(aprovado)
    if self.elementos == []:
      return "Correto"
    return "Incorreto"
      
  
  def camisa(self,elemento):
    return elemento.lower() in {'endrick', 'neymar', 'cr7', 'messi'}
    
  def chuteira(self,elemento):
    return elemento.lower() in {'new balance', 'puma', 'nike', 'adidas'}
  
  def encontrar_camisa(self,chuteira):
    for camisa in self.camisas_encontradas:
      if self.relacao[camisa]==chuteira:
        self.camisas_encontradas.discard(camisa)
        self.aprovados.append(camisa)
        self.aprovados.append(chuteira)
        return True
    return False
  
entrada=input()
pilha=Stack(entrada)
print(pilha.verificar_pilha())
