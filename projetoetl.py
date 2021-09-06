#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import pandera as pa


# In[5]:


dataframe = pd.read_csv("ocorrencia20102020copia - Copia EDITADA.csv" , sep="\t",parse_dates=['ocorrencia_dia'])
dataframe


# In[3]:


dataframe.dtypes


# In[4]:


dataframe.ocorrencia_dia


# In[5]:


dataframe.ocorrencia_dia.dt.month


# In[15]:


datafdataframe = pd.read_csv("ocorrencia20102020copia - Copia EDITADA.csv" , sep="\t",parse_dates=['ocorrencia_dia'], dayfirst=True)
datafdataframe.tail(10)

dataframe.dtypes
dataframe.ocorrencia_dia.dt.month
# In[9]:


dataframe.dtypes

pip install pandera
# In[19]:


schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia": pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade ": pa.Column(pa.String),
        "ocorrencia_uf": pa.Column(pa.String, pa.Check.str_lenght(2,2)),
        "ocorrencia_aerodromo": pa.Column(pa.String),
        "ocorrencia_dia": pa.Column(pa.DateTime),
        "ocorrencia_hora": pa.Column(pa.String, pa_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes": pa.Column(pa.Int)
        
,        
        
    }
)


# In[20]:


schema.validate(dataframe)


# In[21]:


schema.validate(dataframe)


# In[ ]:




