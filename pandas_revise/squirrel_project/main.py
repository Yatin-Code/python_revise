import pandas as pd

df = pd.read_csv("squirrel_project/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
total_fur_color = (df["Primary Fur Color"])


fur_color = {
    "Color":[],
    "Count":[]
}


for i in total_fur_color:
    if pd.notna(i):
        if i in fur_color["Color"]:
            id = fur_color["Color"].index(i)
            fur_color["Count"][id] += 1
        else:
            fur_color["Color"].append(i)
            fur_color["Count"].append(1)

df = pd.DataFrame(fur_color)
print(df)
df.to_csv("squirrel_count.csv")

