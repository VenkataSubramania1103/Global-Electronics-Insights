import pandas as pd
from datetime import datetime
import mysql.connector
import sqlite3
import sqlalchemy

def calculate_age(born):
    today = datetime.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


df_customer=pd.read_csv("C:\\Users\\mypc\\Documents\\GUVI\\GE\\Customers.csv",encoding='unicode_escape')
df_customer.isna().sum()
df1_customer=df_customer[['CustomerKey','Gender','Name','Country','State']]
df1_customer['Age'] = pd.to_datetime(df_customer['Birthday']).apply(calculate_age)
df1_customer.isna().sum()
df1_customer


df_products=pd.read_csv("C:\\Users\\mypc\\Documents\\GUVI\\GE\\Products.csv",encoding='unicode_escape')
df_products.isna().sum()
df_products['Unit Cost USD']=df_products['Unit Cost USD'].str.replace('$','').str.replace(',','')
df_products['Unit Cost USD']=pd.to_numeric(df_products['Unit Cost USD'])
df_products['Unit Price USD']=df_products['Unit Price USD'].str.replace('$','').str.replace(',','')
df_products['Unit Price USD']=pd.to_numeric(df_products['Unit Price USD'])



df_sales=pd.read_csv("C:\\Users\\mypc\\Documents\\GUVI\\GE\\Sales.csv",encoding='unicode_escape')
df_sales.isna().sum()
df1_sales=df_sales[['Order Number','Order Date','CustomerKey','StoreKey','ProductKey','Quantity','Currency Code']]
df1_sales['Order Date']=pd.to_datetime(df1_sales['Order Date'])
df1_sales

df_stores=pd.read_csv("C:\\Users\\mypc\\Documents\\GUVI\\GE\\Stores.csv",encoding='unicode_escape')
df_stores.isna().sum()
df_stores['Open Date']=pd.to_datetime(df_stores['Open Date'])
df_stores['Square Meters'].fillna(0, inplace=True)

df_exc_rates=pd.read_csv("C:\\Users\\mypc\\Documents\\GUVI\\GE\\Exchange_Rates.csv",encoding='unicode_escape')
df_exc_rates.isna().sum()
df_exc_rates['Date']=pd.to_datetime(df_exc_rates['Date'])


df_exc_rates.rename(columns={'Date': 'Order Date','Currency':'Currency Code'}, inplace=True)
df_sales_exc=pd.merge(df1_sales,df_exc_rates,on=['Order Date','Currency Code'])

df_customers_sales_exc=pd.merge(df1_customer,df_sales_exc,on='CustomerKey')
df_stores_sales_exc=pd.merge(df_stores,df_sales_exc,on='StoreKey')
df_products_sales_exc=pd.merge(df_products,df_sales_exc,on='ProductKey')
df_prod_customer_sales=pd.merge(df_customers_sales_exc,df_products,on='ProductKey')

df_prod_customer_sales['Converted Cost in USD']=df_prod_customer_sales['Unit Cost USD']/df_prod_customer_sales['Exchange']
df_prod_customer_sales['Converted price in USD']=df_prod_customer_sales['Unit Price USD']/df_prod_customer_sales['Exchange']
df_products_sales_exc['Converted Cost']=df_products_sales_exc['Unit Cost USD']/df_products_sales_exc['Exchange']
df_products_sales_exc['Converted price']=df_products_sales_exc['Unit Price USD']/df_products_sales_exc['Exchange']

#df_products_sales_exc.to_csv('Merged-Product-Sales-Exc.csv')
#df_stores_sales_exc.to_csv('Merged-Stores-Sales-Exc.csv')
#df_customers_sales_exc.to_csv('Merged-Customers-Sales-Exc.csv')
#df_prod_customer_sales.to_csv('All merged table.csv')

conn = sqlalchemy.create_engine(
'mysql+mysqlconnector://root:12345678@localhost:3306/global_electronics')
df1_customer.to_sql(name="customers",con=conn, if_exists='replace', index=False)
df_products.to_sql(name="products",con=conn, if_exists='replace', index=False)
df1_sales.to_sql(name="sales",con=conn, if_exists='replace', index=False)
df_stores.to_sql(name="stores",con=conn, if_exists='replace', index=False)
df_sales_exc.to_sql(name="sales_exc",con=conn, if_exists='replace', index=False)
df_customers_sales_exc.to_sql(name="customers_sales_exc",con=conn, if_exists='replace', index=False)
df_stores_sales_exc.to_sql(name="stores_sales_exc",con=conn, if_exists='replace', index=False)
df_products_sales_exc.to_sql(name="products_sales_exc", con=conn, if_exists='replace', index=False)
df_prod_customer_sales.to_sql(name="product_customer_sales",con=conn,if_exists='replace',index=False)
