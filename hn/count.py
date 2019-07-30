import read
df = read.load_data()
df_list = df['headline'].tolist()
mask = df['headline'].str.contains(r'^\d+$', na=False)
print(mask)
df.drop(mask['headline'], inplace=True)
all_str = ' '.join(df_list)
print(all_str)
