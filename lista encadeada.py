class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class lista:
    def __init__(self):
        self.inicio = None

    def adicionar(self,valor):
        novo = No(valor)
        
        if self.inicio is None:
            self.inicio = novo

        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo

    def mostrar(self):
        atual = self.inicio

        while atual is not None:
            print(atual.valor, end="->")
            atual = atual.proximo
        print("None")

lista = lista()

while True:
    valor = input("degite um algo a ser adicionado a lista : ")

    if valor.lower() == "pare":
            break

    lista.adicionar (valor)

lista.mostrar()
