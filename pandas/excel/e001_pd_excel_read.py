import pandas as pd
import numpy as np

FILE_EXCEL='/home/christophe/Téléchargements/coalpublic2013.xls'
FILE_EXCEL_2='/home/christophe/Téléchargements/employee.xlsx'
FILE_EXCEL_NEW='/home/christophe/Téléchargements/employee-merge.xlsx'

df = pd.read_excel(FILE_EXCEL)
#print(df.head)
print("\nList of columns:")
print(df.dtypes)
df_emp = pd.read_excel(FILE_EXCEL_2)
print(df_emp.dtypes)
df_emp2 = pd.read_excel(FILE_EXCEL_2, sheet_name=1)
df_emp3 = pd.read_excel(FILE_EXCEL_2, sheet_name=2)

cols = [1, 2, 4]
df2 = pd.read_excel(FILE_EXCEL, usecols=cols)
print("\nRead only specific columns, as", cols)
print(df2)

print("\nAbout 'Production (short tons)' column...")
print(df['Production (short tons)'])
print("    Sum: ",df["Production (short tons)"].sum()) 
print("   Mean: ",df["Production (short tons)"].mean())
print("Maximum: ",df["Production (short tons)"].max())
print("Minimum: ",df["Production (short tons)"].min())

df3 = df.copy()
df3.insert(6, "column1", np.nan)
print("\nAdd a new column, at position 6:")
print(df3.columns)

sum_row=df[["Production (short tons)", "Labor Hours"]].sum()
print("\nAdd summation to a row:")
df_sum=pd.DataFrame(data=sum_row).T # or .transpose()
print(df_sum)
df_sum=df_sum.reindex(columns=df.columns)
print(df_sum)

print("\nLast 10 lines:")
print(df.tail(n=10))

print("\nAdd subtotal of 'Labor Hours' against 'MSHA ID':")
df_sub=df[["MSHA ID","Labor Hours"]].groupby('MSHA ID').sum()
print(df_sub)

print("\nDisplay data only for a specific MSHA ID, as 102901:")
print(df[df["MSHA ID"]==102901])
print("\nDisplay data only for specific MSHA ID, as [102976,103380]:")
print(df[df["MSHA ID"].isin([102976,103380])])
print("\nDisplay data only for specific 'Mine Name':")
print(df.query('`Mine Name` == ["Shoal Creek Mine", "Piney Woods Preparation Plant"]'))

print("\nDisplay data only if true condition on a column, as 'Labour Hours' > 20000 :")
print(df[df["Labor Hours"] > 20000])

print("\nDisplay data only if true condition on a column, as 'Mine Name' starts w/ 'P' :")
print(df[df["Mine Name"].map(lambda x: str(x).startswith('P'))])
print("\nDisplay data only if true condition on a column, as 'Mine Name' starts w/ a digit :")
print(df[df["Mine Name"].map(lambda x: str(x)[:1].isdigit())])

print("\nDisplay data only if true condition on a column, as 'Hire date' > 01-01-07 :")
print(df_emp[df_emp['hire_date'] >='20070101'])
print("\nDisplay employee-df sorted by 'Hire date':")
print(df_emp.sort_values('hire_date'))
print("\nDisplay employee-df between 2 dates, as [2005-1, 2006-12] :")
print(df_emp[(df_emp['hire_date'] >='Jan-2005') & (df_emp['hire_date'] <= 'Dec-2006')])
print("\nDisplay employee-df of a specified year, as 2005 :")
df_tmp = df_emp.set_index(['hire_date'])
print(df_tmp.loc["2005"])
print("\nDisplay employee-df sorted by [first_name(desc), last_name(asc)]:")
print(df_emp.sort_values(by=['first_name','last_name'],ascending=[0,1]))

print("\nConcat data from sheets of employee-df:")
df_tmp = pd.concat([df_emp, df_emp2, df_emp3])
print(df_tmp)
print("\nWrite concatened data into a new Excel file", FILE_EXCEL_NEW)
df_tmp.to_excel(FILE_EXCEL_NEW, index=False)
