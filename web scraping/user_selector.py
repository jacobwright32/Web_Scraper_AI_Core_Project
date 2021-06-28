#%%
import pandas as pd
df = pd.DataFrame({'Date' :['01-01-2020', '02-01-2020'],
                    'Temprature':['23C', '24C']})
df


# %%
test = ['a', 'b', 'c']
x = 0
while x <= 2:
    f = open(test[x]+'.txt','w')
    f.write('hello')
    x += 1
# %%
