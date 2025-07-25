import requests
import json
import pandas as pd

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)
df2 = pd.json_normalize(results)

print(df2)

# Here if I want to find out how many calories are contained in a banana
# print(df2.loc[df2["name"] == 'Banana'].iloc[0]['nutritions.calories'])
 
