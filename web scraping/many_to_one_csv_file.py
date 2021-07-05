#%%
import pandas as pd
df = pd.read_csv('Cleaned Data/United Kingdom_Belfast_Cleaned.csv')
df.rename(columns={ 1:'Maximum_Temprature_(C)', 2: 'Minimum_Temprature_(C)', 3: 'Wind_Speed_(km/h)', 4: 'Wind_Direction', 5: 'Amount_of_Rain_(mm)', 6:'Humidity_(%)', 7: 'Cloud_Coverage_(%)', 8:'Pressure_(mb)'}, inplace=True)

#%%
from sqlalchemy import create_engine 
import pandas as pd
import sqlalchemy

user = 'postgres' 
password = 'rolypoly' 
host = 'database-1.c9ijhw9beyo8.us-east-2.rds.amazonaws.com' 
port = '5432' 
db_name = 'postgres' 
db_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}" 

db = create_engine(db_string) 

df.to_sql('belfast', db,if_exists='replace', index=True)
# %%
df
# %%
