# %%
import pandas as pd

# %%
df = pd.read_csv("../data/pedido.csv")
df

# %%
idade = pd.Series([20, 14, 13, 67, 54, 19, 24])

filtro = idade >= 20

idade[filtro]

# %%
# retorna uma série booleadna
filtro_uf = df['descUF'] == 'São Paulo'

df[filtro_uf]

# %%

# É de SP e pediu ketchup

filtro_sp_ketchup = (df['descUF'] == 'São Paulo') & (df['flKetchup'])
filtro_sp_ketchup

df[filtro_sp_ketchup]

# %%
# negativa
filtro_sp_ketchup = (df['descUF'] == 'São Paulo') & ~(df['flKetchup'] == True)
df[filtro_sp_ketchup]

# %%
# Maneira 1
filtro_ufs_ketchup = ((df['descUF'] == 'São Paulo') | (
    df['descUF'] == 'Rio de Janeiro') | (df['descUF'] == 'Paraná')) & df['flKetchup']
df[filtro_ufs_ketchup]

# %%
df[filtro_ufs_ketchup]['descUF'].unique()

# %%
df[filtro_ufs_ketchup]['flKetchup'].unique()

# %%
# Maneira 2

ufs = ['São Paulo', 'Rio de Janeiro', 'Paraná']
df['descUF'].isin(ufs)

filtro_ufs_ketchup = df['descUF'].isin(ufs) & df['flKetchup']
df[filtro_ufs_ketchup]

# %%
filtro_txt_na = df['txtRecado'].isna()
df[filtro_txt_na]

# %%
