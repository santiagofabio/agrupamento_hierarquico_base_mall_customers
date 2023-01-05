def exploracao_dados(df):
     import pandas as pd
     import seaborn as sns
     import matplotlib.pyplot as plt
     """
     Catalogo de dados 
     CustomerID                 int64
     Genre                     object
     Age                        int64
     Annual Income (k$)         int64
     Spending Score (1-100)     int64
     """
     
     #------------------COUNTPLOT--------------
     sns.countplot(x=df["Genre"])
     plt.title('Genre Customer')
     plt.savefig('Genero.jpg', dpi =300, format ='jpg')
     plt.close()
     
     
    
     
     
     label =["Age", "Annual Income (k$)","Spending Score (1-100)" ] 
     #----------------- BOXPLOT----------------
     plt.tight_layout()
     sns.boxplot(data=df["Age"], orient="h",bootstrap=100  )
     plt.title('Boxplot  Age  ', fontsize=16)
     plt.xlabel('Age', fontsize=14)
     plt.savefig('boxplot_age.jpg',dpi =400, format='jpg') 
     plt.close()
     
     plt.tight_layout()
     sns.boxplot(data=df["Annual Income (k$)"], orient="h",bootstrap=100  )
     plt.title('Boxplot Annual Income (k$)  ', fontsize=16)
     plt.xlabel('Annual Income (k$)', fontsize=14)
     plt.savefig('boxplot_income.jpg',dpi =400, format='jpg') 
     plt.close()
     
     
     plt.tight_layout()
     sns.boxplot(data=df["Spending Score (1-100)"], orient="h",bootstrap=100  )
     plt.title('Boxplot Spending Score (1-100)', fontsize=16)
     plt.xlabel('Spending Score (1-100)', fontsize=14)
     plt.savefig('boxplot_score.jpg',dpi =400, format='jpg') 
     plt.close()
     
    
     label =["Age", "Annual Income (k$)","Spending Score (1-100)" ] 
     from matplotlib.pylab import rcParams
    
     rcParams['figure.figsize']= 16,10
     fig, ((ax1, ax2,ax3)) = plt.subplots(1, 3)
     fig.suptitle('Dados quanitativos', fontsize =16)
     sns.histplot(data =df , x =label[0], ax =ax1, kde=True,  stat='density')
     sns.histplot(data =df , x =label[1], ax =ax2, kde=True,  stat='density')
     sns.histplot(data =df , x =label[2], ax =ax3, kde=True,  stat='density' ) 
     fig.savefig('metricas.jpg', dpi=300, format='jpg')
     plt.tight_layout()
     plt.show() 
     plt.close()
     
   
     
     return(0)
    