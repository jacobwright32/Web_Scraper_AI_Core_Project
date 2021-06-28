#%%
import psycopg2
conn = psycopg2.connect(
	host='database-1.c9ijhw9beyo8.us-east-2.rds.amazonaws.com',
	port=5432,
	dbname='postgres',
	password='rolypoly'
)

# %%
