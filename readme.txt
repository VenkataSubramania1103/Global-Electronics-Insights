Global Electronics Insights Project

This project is for analysing the sales data and providing the insights with Power BI.
We are using Python, MySQL and Power BI for this project

Datasets Used:
Customers 
    CustomerKey, Gender, Name, City, State, Code, State, Zip Code, Country, Continent, Birthday
Exchange_Rates
    Date, Currency, Exchange 
Products
    ProductKey, Product Name, Brand, Color, Unit Cost USD, Unit Price USD, SubcategoryKey, Subcategory, CategoryKey, Category 
Sales
    Order Number, Line Item, Order Date, Delivery Date, CustomerKey, StoreKey, ProductKey, Quantity, Currency Code 
Stores
    StoreKey, Country, State, Square Meters, Open Date

Libraries Used:
Pandas :
    For reading the dataset and merging it as Data frames
Datetime :
    For calculating the age for the Customers
Sqlalchemy :
    For creating a data base connection and loading the data from data frames to SQL as individual tables

We are performing the data pre-processing and Exploratory Data analysis to make the data usable.
Then they are merged based on the foreign key and imported to SQL using Sqlalchemy.

We are using Power BI to visualize the data based on various scenerios of the data.

