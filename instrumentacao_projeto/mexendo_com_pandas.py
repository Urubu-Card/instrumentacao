import pandas as pd


# Series é um transmissor unidimensional rotulado,semelhante a uma coluna de uma tabela

# Cada elemento possui um rótulo (index),Acessa-se elementos com dados['a']

#Acessa-se elementos com dados['a']

dados = pd.Series([10,20,30,40],index=['a','b','c','d'])
print(dados)

# DataFrame é uma tabela bidimensional com linhas e colunas rotuladas.

dados1 = {
    'Nome'      : ["Bermas","JjmySon","DaniHot"],
    "Idade"     : [10000,69,24],
    "Cidade"    : ["Cidade Dos Semens","HoloLandia","Cabare"]
}

df = pd.DataFrame(dados1)
print(df)


# Index são os rotulos que indentificam cada coluna
df.index = ['a','b','c']
print(df)