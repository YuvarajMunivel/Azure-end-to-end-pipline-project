-----------------------
--CREATE VIEWS CALENDER
-----------------------
CREATE VIEW gold.calender
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Calender/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS CUSTOMERS
-----------------------
CREATE VIEW gold.cutomers
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Customers/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS Product_Categories
-----------------------
CREATE VIEW gold.Product_Categories
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Product_Categories/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS Product_Subcategories
-----------------------
CREATE VIEW gold.Product_Subcategories
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Product_Subcategories/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS Products
-----------------------
CREATE VIEW gold.Products
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Products/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS Returns
-----------------------
CREATE VIEW gold.ret
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Returns/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS SALES
-----------------------
CREATE VIEW gold.sales
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Sales/',
            FORMAT = 'PARQUET'

)AS query1


-----------------------
--CREATE VIEWS Tarritories
-----------------------
CREATE VIEW gold.Tarritories
AS
SELECT 
*
FROM OPENROWSET(
            BULK'https://awyuvadatalake.blob.core.windows.net/silver/AdventureWorks_Territories/',
            FORMAT = 'PARQUET'

)AS query1

