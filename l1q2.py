class Node:
  def __init__(self,data):
    self.data= data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0
    
  def append(self, elem):
    if self.head:
      #inserção quando a lista já possui elementos
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next = Node(elem)
      print(f"Node {elem} adicionado")
    else:
      #Pirmeira inserção 
      self.head = Node(elem)
      print(f"Node {elem} adicionado")
    self._size+=1
    
  def remove(self,elem):
    if self.head:
      if self.head.data == elem:
        self.head=self.head.next
        self._size-=1
        return (f"Node {elem} foi removido")
      else:
        anteced = self.head
        pointer = self.head.next
        while(pointer):
          if pointer.data==elem:
            self._size-=1
            anteced.next = pointer.next
            pointer.next = None
            return (f"Node {elem} foi removido")
          anteced = pointer
          pointer = pointer.next 
    return (f"Node {elem} não existe")
            
    
  def __len__(self):
    return self._size
    
  def mapa(self, tam):
    mapa=""
    pointer = self.head
    for i in range(tam):
      if pointer.next:
        mapa += pointer.data + '->'
        pointer = pointer.next
      elif pointer:
        mapa += pointer.data
    print(f"mapa:{mapa}")
    
  def __getitem__(self, index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      
  def empurrar(self, numero):
    if not self.head:
      print(f"Node {numero} não existe")
      return

    pointer = self.head
    anterior = None
    while pointer and pointer.data != numero:
      anterior = pointer
      pointer = pointer.next

    if not pointer:
      print(f"Node {numero} não existe")
      return

    if not pointer.next:
      print(f"Não existe Node depois de {numero}")
      return
    
    if anterior:
      temp = pointer.next
      anterior.next = temp
      pointer.next = temp.next
      temp.next = pointer
    else:
      temp = pointer.next
      pointer.next = temp.next
      temp.next = pointer
      self.head = temp

    print(f"Node {numero} empurrado")
  
  def puxar(self, numero):
    if not self.head:
      print(f"Node {numero} não existe")
      return

    if self.head.data == numero:
      print(f"Não existe Node antes de {numero}")
      return

    anterior = None
    anterior2 =None
    pointer = self.head
    while pointer and pointer.data != numero:
      anterior2 = anterior
      anterior = pointer
      pointer = pointer.next

    if not pointer:
      print(f"Node {numero} não existe")
      return

    if anterior2:
      anterior2.next = pointer
      anterior.next = pointer.next
      pointer.next = anterior
    else:
      anterior.next = pointer.next
      pointer.next = anterior
      self.head = pointer

    print(f"Node {numero} puxado")

lista = LinkedList()
instrucao = input()
while instrucao != "fim!":
  separado = instrucao.split(":")
  if separado[1] == "adicione-me!":
    lista.append(separado[0])
  elif separado[1] == "remova-me!":
    print(lista.remove(separado[0]))
  elif separado[1] == "empurre-me!":
    lista.empurrar(separado[0])
  elif separado[1] == "puxe-me!":
    lista.puxar(separado[0])
  instrucao = input()
  

lista.mapa(len(lista))
