import pandas as pd
from sklearn.datasets import fetch_openml

titanic = fetch_openml(data_id=40945)

data = titanic.data[["pclass","sex", "age", "sibsp", "parch", "fare"]]
target = titanic.target

print(type(data["sex"]))
data["sex"] = data["sex"].cat.rename_categories([1, 0])
data = pd.notna(data)

