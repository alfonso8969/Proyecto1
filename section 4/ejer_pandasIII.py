import pandas as pd


df1 = pd.read_csv("../../../NIVEL0/dataset_2a.csv", index_col="id")
df2 = pd.read_csv("../../../NIVEL0/dataset_2b.csv", index_col="user")
df3 = pd.read_csv("../../../NIVEL0/dataset_2c.csv", index_col="ciudad")

df1
df2
df3

df_usuarios = df1.merge(df2, on="user", how="left")
df_usuarios

df_complete = df_usuarios.merge(df3, on="ciudad", how="left")
df_complete

df_complete['fecha'] = pd.to_datetime(df_complete['fecha_publicado'], format="%d/%m/%Y")

df_complete['mes'] = df_complete['fecha_publicado'].apply(lambda x: x[3:])
df_complete

df_complete.groupby('mes').agg({'user': 'count'})

grouped = df_complete.groupby(['mes', 'ciudad']).agg({'user': 'count'})

ungrouped = grouped.reset_index(1)

pivot = ungrouped.pivot(columns='ciudad', values='user')
# EXISTE UNA FUNCIÓN pivot.droplevel(0, axis=columns) QUE ELIMINA LOS NIVELES DE COLUMNAS QUE NO SEAN NECESARIOS
pivot[['GUAYAQUIL']]

pivot = pivot.fillna(0)

pivot.head()

pivot = pivot.transpose()
pivot.head()