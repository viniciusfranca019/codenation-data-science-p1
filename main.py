#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[38]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    count = black_friday.loc[(black_friday['Age'] == '26-35') & (black_friday['Gender'] == 'F'), ['User_ID']].count()
    return int(count.User_ID)
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return int(black_friday.nunique().User_ID)
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return int(black_friday.dtypes.nunique())
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    mySet = black_friday
    atLeastOneNull = (mySet.count().max() - mySet.count().min()) / mySet.count().max()
    return float(atLeastOneNull)
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    mySet = black_friday.isnull().nunique()
    nullIndex = mySet[mySet > 1].index
    columsWithNull = black_friday[nullIndex].isnull()
    columsWithNull[columsWithNull['Product_Category_3'] == True].count()
    storeData = {}
    highestNum = 0
    for index in nullIndex:
        numberOfNulls = columsWithNull[columsWithNull[index] == True].count()[0]
        storeData[index] = numberOfNulls
    for key in storeData:
        if (storeData[key] > highestNum):
            highestNum = storeData[key]
    return int(highestNum)
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    mySet = black_friday
    return int(mySet['Product_Category_3'].mode())
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    purchaseColum = black_friday['Purchase']
    purchaseMean = purchaseColum.mean()
    purchaseMax = purchaseColum.max()
    purchaseMin = purchaseColum.min()

    def normalize(x):
        result = (x - purchaseMin) / (purchaseMax - purchaseMin)
        return result

    newPurchaseColum = purchaseColum.apply(normalize)
    newMean = newPurchaseColum.mean()
    return float(newMean)
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    purchaseColum = black_friday['Purchase']
    purchaseMean = purchaseColum.mean()
    purchaseStd = purchaseColum.std()

    def padronize(x):
        result = (x - purchaseMean) / purchaseStd
        return result

    newPurchaseColum = purchaseColum.apply(padronize)
    res = newPurchaseColum[((newPurchaseColum > -1) & (newPurchaseColum < 1))].count()
    return res
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    # observe na questão 6 a variavel storedData irá mostrar que a quantidade de null deles são diferentes
    return bool(False)
    pass

