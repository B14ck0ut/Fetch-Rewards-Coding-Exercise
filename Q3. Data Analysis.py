import json
import pandas as pd
import numpy as np

files = ["receipts.json", "users.json", "brands.json"]
for file in files:
    print(file)
    file = "json files/" + file
    # Read file
    with open(file, "r", encoding="utf-8") as f:
        data_list = []
        for line in f:
            data = json.loads(line)
            data_list.append(data)
        df = pd.json_normalize(data_list)
    print(df.dtypes, "\n")
    # Check for missing values
    missing_values_count = df.isnull().sum()
    total_cells = np.product(df.shape)
    total_missing = missing_values_count.sum()
    percent_missing = (total_missing / total_cells) * 100
    if percent_missing > 0:
        print("Missing data found:")
        print(missing_values_count[missing_values_count > 0])
    print("Data missing rate: {:.3f}%\n".format(percent_missing))




