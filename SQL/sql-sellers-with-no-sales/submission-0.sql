SELECT s.seller_name
FROM seller s LEFT JOIN 
    orders o ON
    s.seller_id = o.seller_id
    AND
    EXTRACT(YEAR FROM o.sale_date) = 2020
WHERE 1=1 AND
order_id is NULL
ORDER BY s.seller_name ASC;