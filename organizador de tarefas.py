print("ORGANIZADOR DE TAREFAS!")
print("1- Adicionar Tarefa " + "\n" +
      "2- visualizar Tarefas" + "\n"+
      "3- Remover Tarefa" + "\n" +
      "4- Sair" + "\n")

lista_de_tarefas = []

while True:
    try:   
      opção = int(input("digite a opção escolhida: "))

    except ValueError:
         print("você não digitou um numero!")
         continue

    if ( opção >= 1 and opção <= 4):

      if (opção == 1):
            tarefa = input("digite a sua tarefa: ").strip()

            if(tarefa == ""):
                 print("nenhuma tarefa foi adicionada!")
            else:
                  lista_de_tarefas.append(tarefa)

      elif (opção == 2):
            for indice, tarefas in enumerate(lista_de_tarefas):
                  print(f"posição {indice}: {tarefas}")

      elif (opção == 3):
            for elemento in lista_de_tarefas:
                  print(f"São este os elementos da lista: {elemento}")
            remover = input("digite a tarefa que deseja retirar: ")

            if (remover in lista_de_tarefas):
                  lista_de_tarefas.remove(remover)
            else:
                  print("este elemento não esta na lista!")

      elif (opção == 4):  
            break

    else:
         print("está naão é uma opção valida digite um numero de 1 a 4")
         
for elemento in lista_de_tarefas:
      print(f"Esta é sua lista de tarefas: {elemento}")   
