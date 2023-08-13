# %%
import pandas as pd

# %%
df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido.head(20)

# %%
df_produto = pd.read_csv("../data/produto.csv")
df_produto
df_pedido = pd.read_csv("../data/pedido.csv")
# %%
# Maneira 1
df_join = df_item_pedido.merge(right=df_produto,
                               how='left',
                               on=['descItem'])

df_join.merge(df_pedido, how='left')
# %%
# Maneira 2
df_join = (df_item_pedido.merge(right=df_produto, how='left')
                         .merge(right=df_pedido, how='left'))
df_join
