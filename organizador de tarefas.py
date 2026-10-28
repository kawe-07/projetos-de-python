print("ORGANIZADOR DE TAREFAS!")

lista_de_tarefas = []

while True:
    try:  
      print("-------------------------")
      print("1- Adicionar Tarefa " + "\n" +
      "2- visualizar Tarefas" + "\n"+
      "3- Remover Tarefa" + "\n" +
      "4- Sair" + "\n") 
      opção = int(input("digite a opção escolhida: "))

    except ValueError:
         print("você não digitou um numero!")
         continue
    if ( opção >= 1 and opção <= 4):

      if (opção == 1):
            
            while True:
             print("------------ adicione sua tarefa! --------------")
             tarefa = input("digite a sua tarefa: ").strip()
             if(tarefa == ""):
              print("nenhuma tarefa foi adicionada!")
             else:
                  lista_de_tarefas.append(tarefa)
                  print(f"a tarefa '{tarefa}' foi adcionada com sucesso! ")
                  break

      elif (opção == 2):

            print("------------- suas tarefas! ---------------")
            for indice, tarefas in enumerate(lista_de_tarefas):
                  print(f"posição {indice}: {tarefas}")

      elif (opção == 3):

            if (len(lista_de_tarefas) == 0):
                  print("----------------------")
                  print("Lista Vazia")
            else:
                  print("-------------- sua lista ----------------")
                  for indice, elementos in enumerate(lista_de_tarefas):
                        print(f"posição {indice}: {elementos}")

                  try:
                   remover = int(input("digite o indice da tarefa que deseja retirar: "))
                  except ValueError:
                   print("você não digitou um numero!")
                   continue    

                  if (remover >=0 and remover < len(lista_de_tarefas)):

                        removida = lista_de_tarefas.pop(remover)
                        print("---------- sua nova lista ----------")
                        for indice, elemento in enumerate(lista_de_tarefas):
                              print(f"{indice}: {elemento}")  
                        print(f"A tarefa {removida} foi removida com sucesso!")
                  else:
                        print("este elemento não esta na lista!")

      elif (opção == 4):  
            break
    else:
         print("está não é uma opção valida digite um numero de 1 a 4")

print(f"Esta é sua lista de tarefas: ") 
for indice, elemento in enumerate(lista_de_tarefas):
      print(f"{indice}: {elemento}")  
