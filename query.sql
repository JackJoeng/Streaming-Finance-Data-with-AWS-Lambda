SELECT DISTINCT a.Company, a.Highest_Hourly_Price, CAST(ts AS TIMESTAMP) AS datetime, a.hour
FROM (
    SELECT name AS Company, (EXTRACT(HOUR FROM (CAST(ts AS TIMESTAMP))) - 4) AS hour, max(high) as Highest_Hourly_Price
    FROM finance_data_jack
    GROUP BY 1, 2
    ORDER BY 1, 2
    ) a,
    finance_data_jack b
WHERE a.Company=b.name 
AND a.hour = (EXTRACT(HOUR FROM (CAST(ts AS TIMESTAMP))) - 4)
AND a.Highest_Hourly_Price = b.high
ORDER BY 1, 4
;