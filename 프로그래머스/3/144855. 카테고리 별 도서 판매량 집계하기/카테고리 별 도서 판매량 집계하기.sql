-- 코드를 입력하세요
SELECT
    b.category,
    SUM(bs.sales) as total_sales
FROM
    book b 
    LEFT JOIN book_sales bs ON b.book_id = bs.book_id
WHERE
    DATE_FORMAT(bs.sales_date, '%Y-%m') = '2022-01'
GROUP BY
    b.category
ORDER BY
    b.category ASC;
