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