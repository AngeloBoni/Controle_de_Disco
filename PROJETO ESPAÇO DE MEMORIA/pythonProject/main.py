from function_myself import transform_mb, percent

data = open("dados.txt", "r")
content = data.read()

separed = content.split()
dic = {}

for i in range(len(separed)):
    if i % 2 == 0:
        dic[separed[i]] = separed[i + 1]

soma = 0
for key in dic:
    soma += int(dic[key])

soma = soma / 1048576

dic = transform_mb(dic)
percentual = percent(dic, soma)
lista = []

cont = 1
lista.append("ACME Inc.           Uso do espaço em disco pelos usuários")
lista.append("------------------------------------------------------------------------")
lista.append("Nr.  Usuário        Espaço utilizado     % do uso")
lista.append("                                                                        ")

for key in dic:
    lista.append(f"{cont}.  {key}        {round(dic[key], 2)}mb      {round(percentual[key], 2)}%")
    cont += 1

lista.append("                                                                        ")
lista.append(f"Espaço total ocupado: {round(soma, 2)}mb ")
lista.append(f"Espaço médio ocupado: {round((soma / len(dic)), 2)}mb ")

saida = ""

for elemento in lista:
    saida += "\n" + elemento

arquivo = open("saída.txt", "w")
arquivo.write(
    saida
)
print(saida)
