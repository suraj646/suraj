import pandas as pd
df=pd.read_excel(r"C:\Users\suraj\Desktop\pandas\Customer Call List.xlsx")
df
# remove duplicates 
df=df.drop_duplicates()
df
# removing unwanted column
df=df.drop(columns="Not_Useful_Column")
df
df["Last_Name"]=df["Last_Name"].str.strip("123./_")# putting every thing you want to remove in one
df
df["Phone_Number"]=df["Phone_Number"].str.replace(r'[^a-zA-Z0-9]','',regex=True)#clearing number
df
# now formating 
df["Phone_Number"]=df["Phone_Number"].apply(lambda x:str(x))# first to format the numbers in desired order
df["Phone_Number"]=df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-'+ x[6:10]) #adding - after every 3 numbers
df
# now removing nan and Na
df["Phone_Number"]=df["Phone_Number"].str.replace('nan--','NILL',regex=True)

df["Phone_Number"]=df["Phone_Number"].str.replace('Na--','NILL',regex=True)
df["Phone_Number"]=df["Phone_Number"].str.replace('NIL-L-','NILL',regex=True)
df
df[["Street_address","State","Zip_code"]]=df["Address"].str.split(',',expand=True)
df
df["Do_Not_Contact"]=df["Do_Not_Contact"].replace('Yes','Y')
df["Do_Not_Contact"]=df["Do_Not_Contact"].replace('No','N')
df
df["Paying Customer"]=df["Paying Customer"].replace('Yes','Y')
df["Paying Customer"]=df["Paying Customer"].replace('No','N')
df
df=df.fillna('')# remove nan and none value
df
df.replace('N/a','')
for i in df.index:
    if df.loc[i,"Do_Not_Contact"]=='Y':
        df.drop(i,inplace=True)
df
for i in df.index:
    if df.loc[i,"Phone_Number"]=='NILL':
        df.drop(i,inplace=True)
df
# resetting the index
df=df.reset_index(drop=True)
df# final product
