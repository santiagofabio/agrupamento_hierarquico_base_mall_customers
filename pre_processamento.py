def pre_processamento():
     import pandas as pd
     file = 'Mall_Customers.csv'
     df = pd.read_csv(file, sep=',', encoding='utf-8')
        
     from  sklearn.preprocessing import LabelEncoder, StandardScaler
     df.rename(columns={'Genre': 'genero', 'Age':'idade', 'Annual Income (k$)':'rendimento','Spending Score (1-100)':'pontuacao' }, inplace = True)
     df.drop(columns=['CustomerID'], inplace =True)
     df['genero'] = LabelEncoder().fit_transform(df['genero'])
     
     import pandas as pd
     df.to_csv('df_prepocessado.csv', sep =';', encoding='utf-8', index =False)
     print(df.dtypes)
     
     df2 = df.iloc[:,0:4].values
     df_esc =StandardScaler().fit_transform(df2)
  
     import pickle 
     # Salava os arquivos 
     with open('df_escalonado.pkl','wb') as arquivo:
            pickle.dump( df_esc, arquivo)
 
     
     return(0)