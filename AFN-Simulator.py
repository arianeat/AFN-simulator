# Simulação de um Autômato Finito Não-determinístico


items_automato = {"lista_alfabeto":[], "lista_estados":[], "lista_inicial":[], "lista_finais":[]}
transicoes = {"origem": [], "simbolo": [], "destino": []}

def lerArquivo(arquivo):

    with open(arquivo, "r") as arquivo:

        for linha in arquivo:

            if linha.count("alfabeto"):
                linha = linha.split("=")
                linha = linha[1]
                linha_alfabeto = linha.split(",")

                for i in linha_alfabeto:
                    i = i.strip("\n")
                    items_automato["lista_alfabeto"].append(i)
                items_automato["lista_alfabeto"].append("epsilon")  # adicionando a transição vazia no alfabeto

            if linha.count("estados"):
                linha = linha.split("=")
                linha = linha[1]
                linha_estados = linha.split(",")

                for i in linha_estados:
                    i = i.strip("\n")
                    items_automato["lista_estados"].append(i)

            if linha.count("inicial"):
                linha = linha.split("=")
                linha = linha[1]
                linha_inicial = linha.split(",")

                for i in linha_inicial:
                    i = i.strip("\n")
                    items_automato["lista_inicial"].append(i)

            if linha.count("finais"):
                linha = linha.split("=")
                linha = linha[1]
                linha_finais = linha.split(",")

                for i in linha_finais:
                    i = i.strip("\n")
                    items_automato["lista_finais"].append(i)

            if linha.count("transicoes"):

                for linha in arquivo.readlines():
                    linha_transicao = linha.split(",")
                    transicoes["origem"].append(linha_transicao[0])
                    transicoes["simbolo"].append(linha_transicao[2].strip("\n"))
                    transicoes["destino"].append(linha_transicao[1])
      

def validarAfn():
    validar_afn = []
    if len(items_automato["lista_inicial"]) != 1:
        validar_afn.append(1)
        print("Erro na declaração do estado inicial")

    if items_automato["lista_inicial"][0] not in items_automato["lista_estados"]:
        validar_afn.append(1)
        print("Erro na declaração do estado inicial")

    if items_automato["lista_finais"] != [""]:
        for i in items_automato["lista_finais"]:
            if i not in items_automato["lista_estados"]:
                validar_afn.append(1)
                print("Erro na declaração do estado final")

    for i in transicoes["origem"]:
        if i not in items_automato["lista_estados"]:
            validar_afn.append(1)
            print("Erro na declaração das transições")

    for i in transicoes["simbolo"]:
        if i not in items_automato["lista_alfabeto"]:
            validar_afn.append(1)
            print("Erro na declaração das transições")

    for i in transicoes["destino"]:
        if i not in items_automato["lista_estados"]:
            validar_afn.append(1)
            print("Erro na declaração das transições")

    if len(validar_afn) != 0:
        print("O Autômato é inválido!")
        exit()

    else:
        print("\nAutômato processado com sucesso!")
        # print("Alfabeto =", lista_alfabeto[:-1])
        # print("Estados =",lista_estados)
        # print("Estado Inicial =",lista_inicial)
        # print("Estados Finais =",lista_finais)
        # print("Transições =", transicoes,"\n")


def validarCadeia():
    validar_cadeia = []
    global cadeia

    i = True

    while i:
        print("\nDigite a cadeia de entrada:")
        print("Obs: Para verificar se o autômato aceita a cadeia vazia digite 'epsilon'.")
        cadeia = input()
        if cadeia == "epsilon":
            i = False
        else:
            for i in cadeia:
                if items_automato["lista_alfabeto"].count(i) == 0:
                    print("A cadeia contém símbolos diferentes dos símbolos contidos no alfabeto.")
                    break
                else:
                    i = False


def processarCadeia():
    estados_iniciais = []
    estados_iniciais.append(items_automato["lista_inicial"][0])
    contador_index = -1
    lista_index = []
    lista_destino = []

    # verificando as transições vazias no início do autômato
    for i in estados_iniciais:
        for j in transicoes["origem"]:
            contador_index += 1
            if i == j:
                lista_index.append(contador_index)
        contador_index = -1
        for k in lista_index:
            if transicoes["simbolo"][k] == "epsilon":
                estados_iniciais.append(transicoes["destino"][k])
        lista_index.clear()

    # criando a lista das listas de processamento
    processamento = []
    processamento2 = []

    for i in estados_iniciais:
        processamento.append([i])

    # processando a cadeia

    # verificando se o autômato aceita a cadeia vazia
    if cadeia == "epsilon":
        aceita_vazia = []
        for i in estados_iniciais:
            if i in items_automato["lista_finais"]:
                aceita_vazia.append(i)
        if len(aceita_vazia) > 0:
            print("\nO autômato aceita a cadeia vazia.")
        else:
            print("\nO autômato não aceita a cadeia vazia.")

    # verificando as outras cadeias
    else:
        print("\nSequências de processamento para a cadeia " + cadeia + ":\n")
        for i in cadeia:

            for lista in processamento:

                if len(lista) > 0:
                    for j in transicoes["origem"]:
                        contador_index += 1
                        if lista[-1] == j:
                            lista_index.append(contador_index)
                    contador_index = -1

                    for k in lista_index:
                        if i == transicoes["simbolo"][k]:
                            lista_destino.append(transicoes["destino"][k])
                    lista_index.clear()

                    if len(lista_destino) == 0:
                        for estado in lista:
                            print("", estado, "-", end="")
                        print("-> rejeita")
                        lista.clear()
                    elif len(lista_destino) == 1:
                        lista.append(lista_destino[0])
                    else:
                        for k in lista_destino:
                            lista_copia = list(lista)
                            lista_copia.append(k)
                            processamento2.append(lista_copia)
                        lista.clear()
                    lista_destino.clear()

            for j in processamento2:
                processamento.append(j)
            processamento2.clear()

            # verificando as transições vazias no meio do autômato
            for lista in processamento:

                if len(lista) > 0:
                    for j in transicoes["origem"]:
                        contador_index += 1
                        if lista[-1] == j:
                            lista_index.append(contador_index)
                    contador_index = -1

                    for k in lista_index:
                        if transicoes["simbolo"][k] == "epsilon":
                            lista_destino.append(transicoes["destino"][k])
                    lista_index.clear()

                    if len(lista_destino) > 0:
                        for k in lista_destino:
                            lista_copia = list(lista)
                            lista_copia[-1] = "("+lista_copia[-1]+")"   #para sinalizar o estado de transição vazia na sequência de processamento
                            lista_copia.append(k)
                            processamento.append(lista_copia)
                        lista_destino.clear()

        # verificando as sequências depois do processamento do último dígito da cadeia
        for lista in processamento:
            if len(lista) != 0:
                if lista[-1] in items_automato["lista_finais"]:
                    for estado in lista:
                        print("", estado, "-", end="")
                    print("-> aceita")
                else:
                    for estado in lista:
                        print("", estado, "-", end="")
                    print("-> rejeita")

def novaCadeia():
    print('___________________________________')
    cadeia_nova = input("\nDeseja testar uma nova cadeia? s/n\n").upper()
    if cadeia_nova == "S":
        validarCadeia()
        processarCadeia()
        novaCadeia()
    elif cadeia_nova == "N":
        exit()
    else:
        print("Resposta inválida")
        novaCadeia()


lerArquivo("teste.txt")
validarAfn()
validarCadeia()
processarCadeia()
novaCadeia()
