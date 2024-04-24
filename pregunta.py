"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    df=pd.read_fwf('clusters_report.txt', skiprows=4,index_col=False, names=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])
    
    df['cluster']=df['cluster'].ffill()
    df['cluster']=df['cluster'].astype(int)
    
    df['principales_palabras_clave']=df.groupby(['cluster'])['principales_palabras_clave'].transform(lambda x: " ".join(x))
    df['principales_palabras_clave']=df['principales_palabras_clave'].str.replace(".","")
    
    df=df.drop_duplicates(subset=['cluster'])
    
    df=df.reset_index(drop=True) 
         
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].str.replace("%","")
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].str.replace(",",".")
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].astype(float)
    df['principales_palabras_clave']=df['principales_palabras_clave'].replace(r'\s+'," ",regex=True) 
    df['cantidad_de_palabras_clave']=df['cantidad_de_palabras_clave'].astype(int)
   
    return df
    
