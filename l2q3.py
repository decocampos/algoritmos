class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.level = 0

def inserir(raiz, chave, level=0):
    if raiz is None:
        novo_no = No(chave)
        novo_no.level = level
        return novo_no, level
    else:
        if chave < raiz.chave:
            raiz.esquerda, altura = inserir(raiz.esquerda, chave, level + 1)
        elif chave > raiz.chave:
            raiz.direita, altura = inserir(raiz.direita, chave, level + 1)
        else: 
            raiz.level = level
            return raiz, level
        atualizar_altura(raiz)
        return raiz, altura

def busca_e_torna_raiz(raiz, chave, level=0):
    if raiz is None or raiz.chave == chave:
        if raiz is not None:
            raiz.level = level
            return raiz, level
        else:
            return None, 0
    if chave < raiz.chave:
        raiz.esquerda, nivel_anterior = busca_e_torna_raiz(raiz.esquerda, chave, level + 1)
        if raiz.esquerda is not None:
            if raiz.esquerda.chave == chave:
                return rotacionar_direita(raiz), nivel_anterior
            else:
                raiz.level = level
                atualizar_altura(raiz)
        return raiz, nivel_anterior
    else:
        raiz.direita, nivel_anterior = busca_e_torna_raiz(raiz.direita, chave, level + 1)
        if raiz.direita is not None:
            if raiz.direita.chave == chave:
                return rotacionar_esquerda(raiz), nivel_anterior
            else:
                raiz.level = level
                atualizar_altura(raiz)
        return raiz, nivel_anterior


def rotacionar_direita(y):
    x = y.esquerda
    T2 = x.direita

    x.direita = y
    y.esquerda = T2

    atualizar_altura(y)
    atualizar_altura(x)

    return x

def rotacionar_esquerda(x):
    y = x.direita
    T2 = y.esquerda

    y.esquerda = x
    x.direita = T2

    atualizar_altura(x)
    atualizar_altura(y)

    return y

def atualizar_altura(no):
    altura_esquerda = -1 if no.esquerda is None else no.esquerda.level
    altura_direita = -1 if no.direita is None else no.direita.level
    no.level = 1 + max(altura_esquerda, altura_direita)

def main():
    raiz = None

    while True:
        try:
            operation, value = input().split()
            value = int(value)

            if operation == "ADD":
                raiz, altura = inserir(raiz, value)
                print(altura)
            elif operation == "SCH":
                result, nivel_anterior = busca_e_torna_raiz(raiz, value)
                if result is not None and result.chave == value:
                    raiz = result  # Atualiza a raiz
                    print(nivel_anterior)
                else:
                    print(-1)
        except EOFError:
            break

if __name__ == "__main__":
    main()
