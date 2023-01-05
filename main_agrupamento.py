import numpy as np
import pandas as pd 
from pre_processamento import pre_processamento
from exploracao_dados  import exploracao_dados

# Pre_processamento dos dados
#pre_processamento()
"""
Catalogo de dados 
genero        int32
idade         int64
rendimento    int64
pontuacao     int64
"""
file = 'Mall_Customers.csv'
df = pd.read_csv(file, sep=',', encoding='utf-8')
print(df.dtypes)

exploracao_dados(df)

import pickle
with open('df_escalonado.pkl','rb') as arquivo:
             df_esc = pickle.load(arquivo)


from sklearn.decomposition import PCA
pca = PCA(n_components=2)

df2_pca = pca.fit_transform(df_esc)

#Dendograma 
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage

dendograma = dendrogram(linkage(df2_pca, method='complete' ))
plt.title('Dendograma metodo completo')
plt.savefig('dendograma_completo.jpg', dpi =300, format ='jpg')


dendograma = dendrogram(linkage(df2_pca, method='ward' ))
plt.title('Dendograma metodo ward')
plt.savefig('dendograma_ward.jpg', dpi =300, format ='jpg')


from sklearn.cluster import AgglomerativeClustering
hier = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
classificacao_complete = hier.fit_predict(df2_pca)

import plotly.express as px 
graf =px.scatter(x=df2_pca[:,0], y=df2_pca[:,1],color=classificacao_complete)
graf.update_layout(width =800, height =500, title_text ='Agrupamento Hierarquico')
graf.write_image("agrup_hierarquico.jpg")

agrupamento_completo =pd.DataFrame(classificacao_complete, columns=['Grupos'])
df_classifcado = pd.concat([df,agrupamento_completo], axis =1)
print(df_classifcado.head())
print(df_classifcado.loc[df_classifcado.Grupos==2])