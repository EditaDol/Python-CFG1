import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales.csv")
sales = df["sales"]
expenditure = df["expenditure"]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]

fig, ax = plt.subplots()
ax.set_title("Monthly Sales and Expenditures")
ax.set_xlabel("Months")
ax.set_ylabel("Sale  + Expenditure ")


plt.plot(months, sales, label = "sales")
plt.plot(months, expenditure, label = "expenditure")
plt.legend()
plt.show()
