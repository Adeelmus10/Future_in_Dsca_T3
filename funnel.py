import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("bank-full.csv", sep=';')

# clean
df.columns = df.columns.str.lower()

df.isnull().sum()

df["converted"] = df['y'].map({'yes':1, 'no':0})

df.to_csv("bank-full cleaned.csv", index = False) 

# funnel definition
total_users = len(df)
converted_users = df["converted"].sum()

funnel = pd.DataFrame({
    "Stage": ["Contacted", "Converted"],
    "Users": [total_users, converted_users]})

# funnel visualisation
fig = px.funnel(funnel, x = "Users", y = "Stage", title = "Marketing Funnel Overview")
fig.show()

# conversion rate
Conversion_rate = df["converted"].mean() * 100
print(f"Conversion Rate: {Conversion_rate:.2f}%")

# channel performance analysis
channel_conversion = (df.groupby("contact")["converted"].mean().sort_values(ascending=False) * 100)

channel_conversion.plot(kind = "bar", figsize=(10,4))
plt.title("conversion rate by contact channel")
plt.xticks(rotation=45)
plt.gca().set_facecolor("#a9a9a9")
plt.gcf().set_facecolor("#a9a9a9") 
plt.ylabel("Conversion Rate (%)")
plt.show()

# monthly campaign performance
monthly_conversion = df.groupby("month")["converted"].mean() * 100

monthly_conversion.plot(marker = "o", figsize= (10,4))
plt.title("monthly conversion trend")
plt.gca().set_facecolor("#a9a9a9")
plt.gcf().set_facecolor("#a9a9a9") 
plt.ylabel("conversion rate (%)")
plt.show()

# customer profile analysis
sns.boxplot(data = df, x = "converted", y = "age")
plt.title("age distribution by conversion")
plt.gca().set_facecolor("#a9a9a9")
plt.gcf().set_facecolor("#a9a9a9") 
plt.show()

# drop off analysis
drop_off_rate = 100 - Conversion_rate
print(f"Drop-off Rate: {drop_off_rate:.2f}%")