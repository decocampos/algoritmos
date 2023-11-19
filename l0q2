class Animal:
    def __init__(self):
        self.listaAnimais = []

    def cadastro(self, local, raca, data):
        self.listaAnimais.append((local, raca, data))

    def imprimeRelatorio(self):
        for animal in self.listaAnimais:
            print(f"Local: {animal[0]}\nRaça: {animal[1]}\nData: {animal[2]}\n")

    def dataInteresse(self, data):  
        diaI, mesI, anoI = map(int, data.split("/"))

        for animal in self.listaAnimais:
            dia, mes, ano = map(int, animal[2].split("/"))

            if ano > anoI or (ano == anoI and mes > mesI) or (ano == anoI and mes == mesI and dia > diaI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

    def removerAnimal(self, raca, data):
      animal_para_remover = None
    
      for animal in self.listaAnimais:
          if animal[1] == raca and animal[2] == data:
              animal_para_remover = animal
              break
  
      if animal_para_remover is not None:
          self.listaAnimais.remove(animal_para_remover)
        

sistema = Animal()

continuar = True
while continuar:
    entrada = input()

    if entrada == "1":
        registros = input().split()
        sistema.cadastro(registros[0], registros[1], registros[2])
      
    elif entrada == "2":
        sistema.imprimeRelatorio()
      
    elif entrada == "3":
        data = input()
        sistema.dataInteresse(data)
      
    elif entrada == "4":
        remover = input().split()
        sistema.removerAnimal(remover[0], remover[1])
      
    elif entrada == "5":
        continuar = False
