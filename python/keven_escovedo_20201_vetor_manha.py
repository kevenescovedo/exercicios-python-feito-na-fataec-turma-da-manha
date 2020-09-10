# -*- coding: utf-8 -*-
"""Keven Escovedo - 20201_Vetor_Manha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zCHUwpvWr39mFg-xmQ3EM1HDrsOPW-Le

#**EXERCÍCIOS - V E T O R**

### 1. Faça um algoritmo que calcule e apresente a média de idades de uma sala de 35 alunos.​​
"""

i = 0;

soma = 0;
while i <= 35:
    idade.append(int(input("Digite a idade do aluno:\n")))
    soma = idade[i] + soma
    print(i)
    i = i + 1
media = soma/i
print("a média de soma das idades é de:",media)

"""### 2. Faça um algoritmo que calcule e apresente a média de alturas (vetor) de uma sala de 35 alunos. Informe também quantos alunos e quais (posição) são os que possuem idade (outro vetor) superior a 25 anos.​"""

i = 0;
altura = [];
soma = 0;
contador = 0;
idade = []
while i <= 35:
    idade.append(int(input("Digite a idade do aluno:\n")))
    if idade[i] > 25:
       print("o aluno",i,"´tem uma idade  maior que 25 anos")
       contador = contador + 1
    altura.append(float(input("Digite a altura do aluno:\n")))
   
              
              
    soma = altura[i] + soma
    
    print(i)
    i = i + 1
media = soma/i
print("a média de soma das  alturas é de:",media)
print("a qtd de pessoas maiores que 25 anos é de:",contador)

"""### 3. Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso, encontre qual a pessoa mais gorda e mais magra e apresente o nome e o peso das mesmas.​ **Não utilize as funções: min(), max()**."""

nome = ["keven","Angela","Anselmo","Tiago","Fernando","Juliana","Marcio","Paulo","Ana", "Hercúles"]
massa = [60,65,67,88,78,65,90,78,62,100]
peso_maximo = max(massa)

indice_nome_max = massa.index(peso_maximo)
print(nome[indice_nome_max], "Tem altura maxima de",peso_maximo,"Kg")
peso_minimo = min(massa)
indice_nome_min = massa.index(peso_minimo)

print(nome[indice_nome_min], "Tem altura minima de",peso_minimo,"Kg")

print("-----------------------------------------------------------")
contador = 0;
for peso in massa:
    if contador == 0:
        peso_maior = peso
        peso_menor = peso
    
    else:
        if peso >= peso_maior:
            peso_maior = peso
        elif peso <= peso_menor:
            peso_menor = peso
    contador = contador + 1;
indice_nome_maior = massa.index(peso_maior)
indice_nome_menor = massa.index(peso_menor)
print(nome[indice_nome_maior], "Tem altura maxima de",peso_maior,"Kg")
print(nome[indice_nome_menor], "Tem altura maxima de",peso_menor,"Kg")

"""### 4. Faça um programa que carregue um vetor com nota de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala."""

notas = [10.0,7.5,9.0,8.8,7.8,8.5,9.0,9.8,6.2,7.0]
qtd_mais = 0
qtd_menos = 0
soma = 0;
for n in notas:
  soma = n + soma
divisor = len(notas)
media = soma/10
for nota in notas:
    if nota > media:
        qtd_mais = qtd_mais + 1
    elif nota < media:
        qtd_menos = qtd_menos + 1
print("Houve",qtd_mais,"notas maiores que",media)
print("Houve",qtd_menos,"notas maiores que",media)

"""### 5. Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas posições."""

numeros = [10,7,9,8,12,5,0,2]
for number in numeros:
    if number % 2 == 0:
        print(number,"é par está na posição",numeros.index(number),"do array")

"""### 6. Faça um programa que carregue um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor. Se não conter o nome pesquisado informe que não encontrou. A frase "Não encontrou", quando for o caso deverá ser **apresentada APENAS UMA VEZ**."""

nomes = ["keven","Angela","Anselmo","Tiago","Fernando","Juliana","Marcio","Paulo","Ana", "Hercúles"]
nome_input = input("Escreva o nome para ver se ela está presente em um array:\n")
existe = False
for n in nomes:
  
  if n == nome_input:
    existe = True
    posicao = nomes.index(n)
if existe:
  print(nome_input,"existe")
else:
  print("não existe")

"""### 7. Faça um algoritmo que calcule e apresente a média de alturas superior a 1.80. Informe também quantos e quais (posição) são os alunos."""

alturas = []
maiorqtd = 0;
posicao = [];
soma = 0;
divisor = 0;
media = 0;

resposta = "S"

while resposta == "S":
    alturas.append(float(input("Digite a altura da pessoa:\n")))
    resposta = input("deseja continuar digite S/N:").upper()
    
for altura in alturas:
    if altura > 1.80:
        maiorqtd = maiorqtd + 1
        posicao.append(alturas.index(altura))
        soma = soma + altura
        divisor =  divisor + 1
media = soma/divisor
print("HÁ",maiorqtd," alunos que tem altura maior de 1.80")
print("média de alunos quem tem altura maior que 1.80 é", media)
print("--------------------- posições dos alunos comforme a idade digitada----")
for p in posicao:
    print(p)

"""### 8. Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores, um deles armazenará os elementos positivos e o outro os negativos e ao final apresente-os."""

numeros = []
positivos = []
negativos = []
i = 0;

while i < 10:
    numeros.append(int(input("Digite o numero inteiro:\n")))
    i =  i + 1;

    
for numero in numeros:
   
        if numero > 0:
          positivos.append(numero)
        elif numero < 0:
          negativos.append(numero)
            
print("vetor de numeros negativos", negativos)
print("vetor de numeros positivos", positivos)

"""### 9. Criar um algoritmo que leia dados para um vetor de 100 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. Obs.: percentual = quantidade contada * 100 / quantidade total. **Não devem utilizar as funções: min(), max() e sum()**."""

i = 1;
numeros = []
npar = 0;
nimpar = 0;
soma = 0;

while i <= 100:
    numeros.append(i)
    i = i + 1;
print(numeros)
contador = 0;
for n in numeros:
    
    if contador == 0:
        maior = n
        menor = n
    else:
        if n >= maior:
            maior = n
        elif n <= menor:
            menor = n
    contador = contador + 1;
    soma = n + soma
    if n % 2 == 0:
        npar = npar + 1;
    else:
        nimpar = nimpar + 1;
     

print("Maior número: ",maior)
print("Maior número: ", menor)
print("Percentual de numeros pares: ", (npar * 100)/100)
print("Percentual de numeros impares: ",(nimpar * 100)/100)
print("Média de elementos:", soma/100)

"""### 10. Um vetor é palíndromo se ele não se alterar quando o mesmo for invertido. Por exemplo, o vetor original vo = {1, 3, 5, 2, 2, 5, 3, 1} é palíndromo, pois ele invertido é vi = {1, 3, 5, 2, 2, 5, 3, 1}, igual ao original. Escreva um algoritmo que verifique se um vetor é palíndromo, fazendo comparação de posição por posição do vetor origem (vo) com o vetor invertido(vi). **Não pode usar a função reverse()**."""

vetor = []
i = 1
reverso = []
resposta = "S"
while resposta == "S":
    vetor.append(input("digite um elemento para um vetor:\n"))
    resposta = input("Deseja continuar a inserir se sim diga S e se não diga N:\n").upper()
    

for n in vetor:
    if i == 1:
       reverso.append(vetor[len(vetor)-1])
    else:
         reverso.append(vetor[len(vetor)- i])
    i = i + 1
print(reverso)

if vetor == reverso:
    print("é um palindromo")
else:
    print("não é palindromo")