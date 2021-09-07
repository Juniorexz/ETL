#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[9]:


dataframe = pd.read_csv("ocorrencia20102020copia - Copia EDITADA.csv" , sep="\t",encoding="mbcs",parse_dates=['ocorrencia_dia'])
dataframe.head()


# In[10]:


dataframe.loc[1,'ocorrencia_cidade']


# In[12]:


dataframe.loc[3]


# In[13]:


dataframe.loc[1:3]


# In[16]:


dataframe = pd.read_csv("ocorrencia20102020copia - Copia EDITADA.csv" , sep="\t",encoding="mbcs",parse_dates=['ocorrencia_dia'])
dataframe


# In[19]:


dataframe.loc[:,'ocorrencia_cidade']#Todas as linhas  da ocorrencia cidade


# In[20]:


dataframe.codigo_ocorrencia.is_unique #Alterar o índice,recomendável onde não houver repetição de valores,se é única


# In[22]:


dataframe.set_index('codigo_ocorrencia')#Nesse momento será meu índice


# In[24]:


dataframe.set_index('codigo_ocorrencia', inplace=True)#Após essa alteração será meu índice


# In[26]:


dataframe.head()


# In[27]:


dataframe.loc[40324]


# In[28]:


dataframe.reset_index(drop=True, inplace=True)#voltando ao normal


# In[29]:


dataframe.head()


# In[31]:


dataframe.loc[0, 'ocorrencia_aerodromo']= ''#Alterar dados de **** para vazio


# In[32]:


dataframe.head()


# In[33]:


#Alterar df.loc[:'total_recomendacoes'] = 10 | df.loc[:, 'total_recomendacoes'] = 10


# In[34]:


dataframe['ocorrencia_uf_bkp'] = dataframe.ocorrencia_uf #backup


# In[ ]:


#dataframe.loc[dataframe.ocorrencia_uf == 'SP', ['ocorrencia_classificacoa']] = 'GRAVE' Alterar todos os SP para GRAVE


# In[37]:


dataframe.loc[dataframe.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA #limpar dados


# In[38]:


dataframe.head()


# In[39]:


dataframe


# In[40]:


dataframe.replace(['**','NULL', 'NaN','####','*****','###!'], pd.NA, inplace=True)


# In[41]:


dataframe.tail()


# In[43]:


dataframe.isna().sum()#Saber quantidade de dados não informados


# In[44]:


dataframe.isnull().sum()#Saber quantidade de dados não informados


# In[45]:


dataframe.fillna(0).sum()#Inserir valor 0 em  dados não informados


# In[46]:


dataframe.fillna(10 , inplace = True)#Inserir valor permanente de dados não informados onde houver na


# In[47]:


dataframe['total_recomendacoes_bkp'] = df.total_recomendacoes #Criar um backup e passar os valores da coluna citada


# In[48]:


dataframe.drop(['Unnamed'], axis=9, inplace=True)


# In[49]:


dataframe.dropna() Exclui todos os valores das linhas  da visualização não informados


# In[ ]:


dataframe.dropana(subset=['coluna'])


# In[ ]:


dataframe.drop_duplicates()#remover valores duplicados


# In[ ]:


dataframe.drop_duplicates(inplace=True)#remover valores duplicados dataframe


# In[ ]:





# In[ ]:




