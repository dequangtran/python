import pandas as pd
import os


inputfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flight_plans.csv")
df = pd.read_csv(inputfile)

print(df)
print(df[df["FlightID"] == "F123"].count())