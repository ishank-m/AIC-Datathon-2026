import pandas as pd
import matplotlib.pyplot as plt
import urllib.request as urllib
import openpyxl as openpyxl



file_path = "tuitons.xlsx"
df = pd.read_excel(file_path, sheet_name="Table CP-2")
df_clean = df.iloc[31:57, [0,3]]
df_clean.columns = ["year", "tuition"]
df_clean.to_csv("tuition_clean.csv", index=False)


file_path = "loans_and_grants.xlsx"
df = pd.read_excel(file_path, sheet_name="Table SA-3")
df_clean = df.iloc[66:91, [0,5,7]]
df_clean.columns = ["year", "aid", "loan"]
df_clean["aid"] = df_clean["aid"].round(0).astype(int)
df_clean["loan"] = df_clean["loan"].round(0).astype(int)
df_clean.to_csv("aid_and_loands_clean.csv", index=False)