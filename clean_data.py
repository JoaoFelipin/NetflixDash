import pandas as pd 

df = pd.read_csv("C:/Users/anali/Downloads/netflix_titles.csv")

def clean_data(data):
    data['directo'].fillna('No director',inplace=True)
    data['cast'].fillna('No cast',inplace=True)
    data['country'].fillna('No country',inplace=True)
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    
    data['date_added']=pd.to_datetime(data['data_added'].str.strip())
    
    
    return data 
