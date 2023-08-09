# %%
import pandas as pd
# %%
df = pd.read_csv("../data/pedido.csv")
df
# %%
# Maneira 1
df = df.rename(columns={"descUF": "descEstado"})

# %%
# Maneira 2
df.rename(columns={"descUF": "descEstado"}, inplace=True)
