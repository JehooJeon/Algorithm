-- 코드를 작성해주세요
SELECT
    ii.item_id,
    ii.item_name
FROM
    item_info ii
LEFT JOIN
    item_tree it ON ii.item_id = it.item_id
WHERE
    it.parent_item_id IS NULL
ORDER BY
    ii.item_id;