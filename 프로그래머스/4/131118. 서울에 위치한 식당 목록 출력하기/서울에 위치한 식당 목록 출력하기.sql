-- 코드를 입력하세요
SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO AS I, REST_REVIEW AS R
WHERE I.REST_ID = R.REST_ID AND I.ADDRESS LIKE "서울%"
GROUP BY I.REST_ID
ORDER BY AVG(REVIEW_SCORE) DESC, FAVORITES DESC