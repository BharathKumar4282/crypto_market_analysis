CREATE DATABASE crypto_db;

USE crypto_db;

CREATE TABLE crypto_table (
    id VARCHAR(50),
    symbol VARCHAR(10),
    name VARCHAR(100),
    current_price DECIMAL(18,8),
    market_cap BIGINT,
    total_volume BIGINT,
    price_change_percentage_24h DECIMAL(10,4),
    last_updated DATETIME
);

select * from crypto_table;

-- TOP 5 COINS BY MARKET CAP
select name,symbol,market_cap
from crypto_table
order by market_cap desc
limit 5;

-- TOP 10 CURRENT PRICE COINS
select 
name,
symbol,
current_price
from crypto_table
order by current_price desc
limit 10;

-- VOLATILITY TRENDS
SELECT
    name,
    DATE(last_updated) AS date,
    ABS(price_change_percentage_24h) AS volatility
FROM crypto_table;




