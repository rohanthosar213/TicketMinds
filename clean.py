import pandas as pd

df=pd.read_csv('tickets.csv')
print(df)
print(df.head())
print(f"\nTotal:{len(df)}")
print(df['category'].value_counts())

#Cleaning
df['text'] = df['text'].astype(str).str.lower().str.strip()
df['category'] = df['category'].str.strip()
df = df[df['text'] != 'nan']
df = df[df['text'] != ' ']
df = df.drop_duplicates()

print("after cleaning:")
print(df.head())
print(f"Total: {len(df)}")
print(df['category'].value_counts())

df.to_csv('clean_tickets.csv', index=False)
print("\nclean_tickets.csv ready")
