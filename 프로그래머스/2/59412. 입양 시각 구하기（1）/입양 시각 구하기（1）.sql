-- 코드를 입력하세요
-- SELECT TO_CHAR(DATETIME,'HH24') AS HOUR, COUNT(*) FROM ANIMAL_OUTS
-- GROUP BY TO_CHAR(DATETIME,'HH24')
-- HAVING TO_CHAR(DATETIME, 'HH24') > '08'
-- ORDER BY 1

-- SELECT HOUR(DATETIME) AS HOUR, COUNT(*) FROM ANIMAL_OUTS
-- GROUP BY HOUR(DATETIME) HAVING HOUR(DATETIME) BETWEEN 9 AND 19

--시간을 추출하는 함수들: YEAR, MONTH, HOUR

-- SELECT HOUR(DATETIME) AS 'HOUR', COUNT(*) AS 'COUNT'
-- FROM ANIMAL_OUTS
-- WHERE HOUR(DATETIME) >=9
-- GROUP BY HOUR(DATETIME)
-- ORDER BY 1

SELECT EXTRACT(HOUR FROM CAST(DATETIME AS TIMESTAMP)) AS HOUR, COUNT(*) 
FROM ANIMAL_OUTS
WHERE EXTRACT(HOUR FROM CAST(DATETIME AS TIMESTAMP))  BETWEEN 9 AND 19
GROUP BY EXTRACT(HOUR FROM CAST(DATETIME AS TIMESTAMP))
ORDER BY HOUR
