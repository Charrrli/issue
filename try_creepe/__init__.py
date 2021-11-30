import pandas as pd
import requests
data = pd.read_csv("../data/raw_data.csv",nrows = 1)
target = data.comments_url[0]
json_data = requests.get(target)
for i in json_data.json():
    print(i)
    print("\n")