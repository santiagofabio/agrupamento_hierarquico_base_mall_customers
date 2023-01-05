#### 1. Descrição do projeto
 <p>
 Este projeto tem como  objetivo identificar grupos bem definidos de consumidores a partir dos dados de renda, idade, genero e Score. Para a realização do agrupamento foi empregado o algoritmo PCA (Principal component analysis) a fim de selecionar as duas componetes de maior relevancia, em seguida foi empregado o
 algoritmo AgglomerativeClustering da biblioteca sklearn.cluster , com parametros:
 </p>

 * n_clusters=3
 * affinity='euclidean'  
 * linkage='complete'

#### 2. Catalogo de dados

|Dados| Tipo|
|-----|-----|
|CustomerID|int64|
|Genre| object|
|Age|int64|
|Annual Income (k$)| int64|
|Spending Score (1-100)| int64|

#### 3. Exploção de dados

##### 3.1 Contagem por genero
![Genero](Genero.jpg)
##### 3.2  Boxplot
![boxplot_Age](boxplot_age.jpg)

![boxplot_income](boxplot_income.jpg)

![boxplot_score](boxplot_score.jpg)

##### 3.2  Histograma
![metricas](metricas.jpg)

#### 4 Dendograma
![dendograma_completo](dendograma_completo.jpg)
#### 5 Agrupamento hierarquio

![Dendograma](agrup_hierarquico.jpg)

#### 6 Resultado com 2 Grupos
![grupos](grupos.JPG)