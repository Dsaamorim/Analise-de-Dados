#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Passo 1: Importar a base de dados
import pandas as pd
tabela = pd.read_csv("telecom_users.csv")
#Passo 2: Visualizar a base de dados
#Passo 3: Corrigir a coluna dtype e unnamed

tabela = tabela.drop("Unnamed: 0",axis = 1)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

tabela = tabela.dropna(how = "all", axis = 1)

tabela = tabela.dropna(how = "any", axis = 0)
#Passo 4: Como estão nossos cancelamentos 

display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Passo 5: Vamos olhar cada característica do seu cliente e ver como aquela característica impacta no cancelamento

import plotly.express as px

for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()


# 

# In[ ]:




