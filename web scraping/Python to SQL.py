
# %%
from sqlalchemy import create_engine 
import pandas as pd
import sqlalchemy
import psycopg2
import sys
import boto3
import os
from os import walk
from os import listdir
from os.path import isfile, join
mypath = 'Cleaned Data' 
all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(all_files)


user = 'postgres' 
password = 'rolypoly' 
host = 'database-1.c9ijhw9beyo8.us-east-2.rds.amazonaws.com' 
port = '5432' 
db_name = 'postgres' 
db_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}" 
x = 0
y = len(all_files)
db = create_engine(db_string) 
for file in all_files: 
    df = pd.read_csv('Cleaned Data/' + file)
    df.to_sql('world_city_weather', db,if_exists='append', index=False)
    x += 1
    files_left = len(all_files) - x
    print('There are ' + str(files_left) + ' files_left')

# %%

# %%
