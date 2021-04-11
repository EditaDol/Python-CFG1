import pandas as pd
import statistics
# read data from csv
df = pd.read_csv("sales.csv")
print(df)

# Print sales
month_sales = df[["month", "sales"]]
print(month_sales)

# Total sales
total = sum(df["sales"])
print('Total sales: {}'.format(total))

# Average sales
average = statistics.mean(df["sales"])
print('Average is: {}'.format(round(average)))

# Percentage difference in sales
percentage_sales = df["sales"].pct_change()
print(percentage_sales)
df = pd.read_csv("sales.csv")
df["Percentage difference"] = percentage_sales
df.to_csv("sales.csv", index=False)

# Minimum sale
arr = month_sales.to_records()
minimum = min(arr, key=lambda month: month[-1])
print("The month with min sales is {}".format(minimum))
# Maximum sale

arr = month_sales.to_records()
maximum = max(arr, key=lambda month: month[-1])
print("The month with max sales is {}".format(maximum))

