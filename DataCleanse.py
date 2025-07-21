import pandas as pd

df = pd.read_csv('NYResturantRaw.csv') #import raw csv file

'''----- FUNCTION TO CLEAN DATA -----'''
def clean_data(df):
    df['CAMIS'] = pd.to_numeric(df['CAMIS'], errors='coerce') 
    df['ZIPCODE'] = pd.to_numeric(df['ZIPCODE'], errors='coerce')
    df['PHONE'] = pd.to_numeric(df['PHONE'], errors='coerce')
    df['INSPECTION_DATE'] = pd.to_datetime(df['INSPECTION_DATE'], errors='coerce')
    df['BUILDING'] = pd.to_numeric(df['BUILDING'], errors='coerce')
    df = df[df['INSPECTION_DATE'] != pd.Timestamp('1900-01-01')]
    df.to_csv('NYResturantClean.csv', index = False)

    return df

clean_data(df)



