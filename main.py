import plotly.express as px
import csv

with open("cups of coffee vs hours of sleep.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
      fig.show()


with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="temperature",y="ice cream sale")
    fig.show()
    