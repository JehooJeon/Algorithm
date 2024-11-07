-- 코드를 입력하세요
SELECT
    b.category,
    SUM(bs.sales) as total_sales
FROM
    book b 
    LEFT JOIN book_sales bs 
    ON b.book_id = bs.book_id
WHERE 1 = 1
    AND YEAR(bs.sales_date) = 2022
    AND MONTH(bs.sales_date) = 1
GROUP BY
    b.category
ORDER BY
    b.category ASC;