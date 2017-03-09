import pandas as pd
df = pd.read_excel("bikes.xlsx", sheetname= 0)
# or using sheet index starting 0
#df = pandas.read_excel(open('your_xls_xlsx_filename','rb'), sheetname=2)
# DataFrame = pd.read_excel("PATH\FileName.xlsx", sheetname=0)
df.head()
print (df)

