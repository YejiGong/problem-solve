-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER JOIN USED_GOODS_BOARD ON USED_GOODS_BOARD.WRITER_ID = USED_GOODS_USER.USER_ID
WHERE USED_GOODS_BOARD.STATUS='DONE'
GROUP BY WRITER_ID HAVING SUM(PRICE)>=700000
ORDER BY TOTAL_SALES ASC